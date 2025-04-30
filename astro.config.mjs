import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import compress from '@playform/compress';
import mdx from '@astrojs/mdx';
import icon from "astro-icon";

// Import /static for a static site
import vercelStatic from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
  site: 'https://berlin.pyladies.com',
  integrations: [tailwind(), compress(), mdx(), icon()],
  i18n: {
    locales: ["en", "en"],
    defaultLocale: "en",
    routing: {
      prefixDefaultLocale: false
    }
  },
  // Must be 'static' or 'hybrid'
  output: 'static',
  adapter: vercelStatic(),
});
