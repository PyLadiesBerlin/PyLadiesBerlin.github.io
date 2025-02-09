import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import compress from '@playform/compress';
import mdx from '@astrojs/mdx';

// Import /static for a static site
import vercelStatic from '@astrojs/vercel/static';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind(), compress(), mdx()],
  // Must be 'static' or 'hybrid'
  output: 'static',
  adapter: vercelStatic(),
});
