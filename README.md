# @dau-dev/branding

dau brand identity, design tokens, theme system, and reusable Svelte components.

See [`BRAND.md`](./BRAND.md) for the canonical brand guide.

## Install

The package is not published to npm. Sibling apps link it locally:

```jsonc
// website/package.json
"devDependencies": {
  "@dau-dev/branding": "file:../dau-branding"
}
```

Run `pnpm build` here first so `dist/` exists.

Import the fonts and tokens once at the application root:

```css
@import '@dau-dev/branding/fonts.css';
@import '@dau-dev/branding/tokens.css';
```

Logo files (SVG and PNG, dark and light mode) ship under
`@dau-dev/branding/assets/logo/`; see BRAND.md for the list. The favicon is
`@dau-dev/branding/assets/favicon.svg`.

```svelte
<script lang="ts">
  import { BrandMark, ThemeToggle } from '@dau-dev/branding';
</script>

<BrandMark />
<ThemeToggle />
```

Components: `BrandMark`, `Button`, `CookieNotice`, `SpecTable`, `Split`,
`ThemeToggle`. See BRAND.md for when to use each.

## Develop

```bash
pnpm install
pnpm dev
pnpm check
pnpm lint
pnpm fix
pnpm test
pnpm build
```

After customizing the showcase, run `pnpm test:e2e:update` once to establish its visual baseline.
