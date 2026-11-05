<script lang="ts">
  import type { Snippet } from 'svelte';

  interface Props {
    /** Label for the left half, which uses the page's own surface. */
    hardwareLabel?: string;
    /** Label for the right half, which uses the inverse surface. */
    softwareLabel?: string;
    /** What runs on the device. */
    hardware: Snippet;
    /** What stays in software. */
    software: Snippet;
  }

  let { hardwareLabel = 'Hardware', softwareLabel = 'Software', hardware, software }: Props = $props();
</script>

<div class="split">
  <div class="half page">
    <p class="label">{hardwareLabel}</p>
    {@render hardware()}
  </div>
  <div class="half dau-inverse">
    <p class="label">{softwareLabel}</p>
    {@render software()}
  </div>
</div>

<style>
  .split {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    border: 1px solid var(--dau-border);
  }

  .half {
    min-width: 0;
    color: var(--dau-fg);
    padding: clamp(1.5rem, 4vw, 3.5rem);
  }

  .page {
    background: var(--dau-bg);
  }

  .label {
    margin: 0 0 1.25rem;
    color: var(--dau-fg-muted);
    font-family: var(--dau-font-mono);
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  @media (max-width: 40rem) {
    .split {
      grid-template-columns: 1fr;
    }
  }
</style>
