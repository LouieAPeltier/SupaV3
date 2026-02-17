import { defineConfig } from '@pandacss/dev';

export default defineConfig({
  preflight: true,
  include: ['./src/**/*.{js,jsx,ts,tsx,svelte}'],
  outdir: 'styled-system',
  theme: {
    extend: {
      tokens: {
        colors: {
          primary: {
            value: '#ff6a00'
          },
          primarySoft: {
            value: '#ffd8bf'
          },
          ink: {
            value: '#1f1f1f'
          }
        }
      }
    }
  }
});
