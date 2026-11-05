<script lang="ts">
  interface Props {
    /** Link target. Pass null to render the mark without a link. */
    href?: string | null;
    /** `chip` is the full mark; `disk` drops the package for sizes under 32px. */
    variant?: 'chip' | 'disk';
    /** Rendered height of the mark in px. */
    size?: number;
    /** Show the `dau.` wordmark beside the mark. */
    wordmark?: boolean;
  }

  let { href = '/', variant = 'chip', size = 32, wordmark = true }: Props = $props();
</script>

{#snippet mark()}
  <svg class="mark" width={size} height={size} viewBox="0 0 64 64" aria-hidden="true" focusable="false">
    {#if variant === 'chip'}
      <path
        class="package"
        d="M10 22H4M10 32H4M10 42H4M54 22h6M54 32h6M54 42h6M22 10V4M32 10V4M42 10V4M22 54v6M32 54v6M42 54v6"
        stroke-width="2"
        stroke-linecap="square"
      />
      <rect class="package body" x="10" y="10" width="44" height="44" rx="2" stroke-width="2" />
      <circle class="disk" cx="32" cy="32" r="12" stroke-width="2" />
      <path class="lit" d="M32 20a12 12 0 0 0 0 24z" />
    {:else}
      <circle class="disk" cx="32" cy="32" r="29" stroke-width="4" />
      <path class="lit" d="M32 3a29 29 0 0 0 0 58z" />
    {/if}
  </svg>
  {#if wordmark}
    <span class="word" style:font-size="{Math.round(size * 0.72)}px">dau<b>.</b></span>
  {/if}
{/snippet}

{#if href === null}
  <span class="brand" role="img" aria-label="dau">{@render mark()}</span>
{:else}
  <a class="brand" {href} aria-label="dau home">{@render mark()}</a>
{/if}

<style>
  .brand {
    display: inline-flex;
    align-items: center;
    gap: 0.5em;
    color: var(--dau-fg);
    text-decoration: none;
  }

  .package {
    stroke: var(--dau-fg);
    fill: none;
  }

  .body {
    fill: var(--dau-bg);
  }

  .disk {
    fill: var(--dau-bg);
    stroke: var(--dau-fg);
  }

  .lit {
    fill: var(--dau-fg);
  }

  .word {
    font-family: var(--dau-font-sans);
    font-weight: 300;
    letter-spacing: -0.04em;
    line-height: 1;
  }

  .word b {
    font-weight: 800;
  }
</style>
