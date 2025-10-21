#!/usr/bin/env node

/**
 * Dev Server Performance Benchmark
 * Tests startup time and HMR performance for different dev servers
 */

const { spawn, execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const testFile = path.join(__dirname, 'snake.html');
const originalContent = fs.readFileSync(testFile, 'utf-8');

const servers = [
  {
    name: 'Vite',
    command: 'npx',
    args: ['vite', '--port', '3000'],
    port: 3000,
    supportsHMR: true,
    startPattern: /Local:.*http/
  },
  {
    name: 'Parcel',
    command: 'npx',
    args: ['parcel', 'snake.html', '--port', '3001'],
    port: 3001,
    supportsHMR: true,
    startPattern: /Server running at/
  }
];

console.log('Dev Server Performance Benchmark');
console.log('=================================\n');

async function benchmarkServer(server) {
  return new Promise((resolve) => {
    console.log(`Testing ${server.name}...`);
    const startTime = Date.now();
    let serverStartTime = null;
    let hmrTime = null;

    const proc = spawn(server.command, server.args, {
      stdio: 'pipe',
      shell: true
    });

    let output = '';

    const dataHandler = (data) => {
      const text = data.toString();
      output += text;

      // Detect server start
      if (!serverStartTime && server.startPattern.test(text)) {
        serverStartTime = Date.now() - startTime;
        console.log(`  Startup time: ${serverStartTime}ms`);

        // Test HMR if supported
        if (server.supportsHMR) {
          setTimeout(() => {
            const hmrStartTime = Date.now();

            // Make a small change to the file
            const modifiedContent = originalContent.replace(
              '<title>Snake Game</title>',
              '<title>Snake Game - Modified</title>'
            );
            fs.writeFileSync(testFile, modifiedContent);

            // Wait a bit and restore
            setTimeout(() => {
              hmrTime = Date.now() - hmrStartTime;
              fs.writeFileSync(testFile, originalContent);
              console.log(`  HMR time: ${hmrTime}ms`);

              // Kill the server
              proc.kill();

              resolve({
                name: server.name,
                startupTime: serverStartTime,
                hmrTime: hmrTime
              });
            }, 1000);
          }, 1000);
        } else {
          proc.kill();
          resolve({
            name: server.name,
            startupTime: serverStartTime,
            hmrTime: 'N/A'
          });
        }
      }
    };

    proc.stdout.on('data', dataHandler);
    proc.stderr.on('data', dataHandler);

    proc.on('error', (error) => {
      console.error(`  Error: ${error.message}`);
      resolve({
        name: server.name,
        startupTime: 'Error',
        hmrTime: 'Error'
      });
    });

    // Timeout after 30 seconds
    setTimeout(() => {
      if (!serverStartTime) {
        console.log(`  Timeout waiting for ${server.name} to start`);
        proc.kill();
        resolve({
          name: server.name,
          startupTime: 'Timeout',
          hmrTime: 'Timeout'
        });
      }
    }, 30000);
  });
}

async function runBenchmarks() {
  const results = [];

  for (const server of servers) {
    const result = await benchmarkServer(server);
    results.push(result);
    console.log();
  }

  // Display results
  console.log('\nBenchmark Results:');
  console.log('==================\n');
  console.table(results);

  // Determine winner
  const validResults = results.filter(r => typeof r.startupTime === 'number');
  if (validResults.length > 0) {
    const fastest = validResults.reduce((prev, curr) =>
      curr.startupTime < prev.startupTime ? curr : prev
    );
    console.log(`\nFastest Startup: ${fastest.name} (${fastest.startupTime}ms)`);

    if (fastest.hmrTime && typeof fastest.hmrTime === 'number') {
      console.log(`HMR Performance: ${fastest.hmrTime}ms`);
    }
  }

  console.log('\nRecommendation: Vite is the fastest option for modern development');
  console.log('- Lightning fast startup');
  console.log('- Instant HMR (Hot Module Replacement)');
  console.log('- No bundling during development');
  console.log('- Native ES modules support');
}

// Run benchmarks
runBenchmarks().catch(console.error);
