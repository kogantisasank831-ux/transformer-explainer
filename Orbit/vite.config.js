import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';

const root = fileURLToPath(new URL('.', import.meta.url));

// Orbit can live below another application without inheriting its tooling.
export default defineConfig({
  root,
  css: { postcss: { plugins: [] } },
  server: { fs: { strict: true, allow: [root] } },
});
