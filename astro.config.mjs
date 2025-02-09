import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import compress from '@playform/compress';

// Import /static for a static site
import vercelStatic from '@astrojs/vercel/static';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind(), compress()],
  // Must be 'static' or 'hybrid'
  output: 'static',
  adapter: vercelStatic(),
});
