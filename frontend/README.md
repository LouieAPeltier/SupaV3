# ListRank Frontend (Svelte + Panda CSS ready)

## Quickstart (works in restricted dev containers)

```bash
npm install
npm run dev
```

## Panda CSS in restricted environments

Some managed dev environments/proxies block scoped npm packages such as `@pandacss/dev` with HTTP 403.

If that happens, the app still runs without Panda because styling is currently standard CSS.

When your registry policy allows it, enable Panda manually:

```bash
npm install -D @pandacss/dev
npm run panda:codegen
```

If you use an internal npm proxy, configure scoped registry routing in `.npmrc`:

```ini
@pandacss:registry=https://registry.npmjs.org/
```

## Notes

- Orange (`#ff6a00`) is the primary theme color.
- Firebase web SDK is wired via `src/lib/firebase.ts` and `VITE_` env variables.
- Panda config exists in `panda.config.ts` and can be activated once package access is available.
