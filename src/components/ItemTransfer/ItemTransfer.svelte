<script lang="ts">
    let {imageUrl, shouldMove = false} = $props();
</script>
<div class="itemTransfer">
    <div class={`item ${shouldMove ? 'move' : 'default'}`} style:background={`url('${imageUrl}')`}></div>
</div>
<style>
    .itemTransfer {
        width: 500px;
        height: 125px;
    }

    .default {
        display: none;
    }

    .item {
        background-size: contain !important;
        width: 120px;
        height: 125px;
    }

    .move {
        animation: movingAnim 1s ease-in infinite;
    }

    @keyframes movingAnim {
        from {
            margin-left: 0;
        }
        to {
            margin-left: 150px;
        }
    }
</style>