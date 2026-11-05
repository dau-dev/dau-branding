<script lang="ts" module>
  export interface SpecRow {
    key: string;
    value: string;
    note?: string;
  }
</script>

<script lang="ts">
  interface Props {
    rows: SpecRow[];
    caption?: string;
    /** Column headings; defaults suit a parameter/value datasheet. */
    headings?: [string, string, string?];
  }

  let { rows, caption, headings = ['Parameter', 'Value'] }: Props = $props();
  const withNotes = $derived(rows.some((row) => row.note));
</script>

<div class="wrap">
  <table>
    {#if caption}<caption>{caption}</caption>{/if}
    <thead>
      <tr>
        <th scope="col">{headings[0]}</th>
        <th scope="col">{headings[1]}</th>
        {#if withNotes}<th scope="col">{headings[2] ?? 'Note'}</th>{/if}
      </tr>
    </thead>
    <tbody>
      {#each rows as row (row.key)}
        <tr>
          <th scope="row">{row.key}</th>
          <td>{row.value}</td>
          {#if withNotes}<td class="note">{row.note ?? ''}</td>{/if}
        </tr>
      {/each}
    </tbody>
  </table>
</div>

<style>
  .wrap {
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-family: var(--dau-font-mono);
    font-size: 0.8125rem;
    font-variant-numeric: tabular-nums;
  }

  caption {
    padding-bottom: 0.75rem;
    color: var(--dau-fg-muted);
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    text-align: left;
    text-transform: uppercase;
  }

  th,
  td {
    padding: 0.55rem 1rem 0.55rem 0;
    border-bottom: 1px solid var(--dau-border);
    text-align: left;
    vertical-align: top;
  }

  thead th {
    color: var(--dau-fg-muted);
    font-weight: 400;
  }

  tbody th {
    color: var(--dau-fg-muted);
    font-weight: 400;
    white-space: nowrap;
  }

  .note {
    color: var(--dau-fg-muted);
  }
</style>
