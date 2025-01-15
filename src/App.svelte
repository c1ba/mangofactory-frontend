<script lang="ts">
  import { onMount } from 'svelte';
	import Blacksmith from './components/Blacksmith/Blacksmith.svelte';
	import ItemTransfer from './components/ItemTransfer/ItemTransfer.svelte';
	import Miner from './components/Miner/Miner.svelte';
	import Smelter from './components/Smelter/Smelter.svelte';
	import Storage from './components/Storage/Storage.svelte';

	type WebsocketData = {
		message: string;
		obj: unknown;
		action: string;
		qty: number;
		mat: "Iron";
		item: "Ore" | "Ingots" | "Pipes"
	}
	
	let isOreTransfering = false
	let isIngotTransfering = false
	let isPipeTransfering = false
	let websocketMsg = ''
	onMount(() => {
		const socket = new WebSocket(`ws://localhost:8765`);
		// Connection opened
		socket.addEventListener('open', () => {
    		console.log("It's open");
		});

		// Connection opened
		socket.addEventListener('error', (error) => {
    		console.error(`Error occured:\n${error}`);
		});

		// Listen for messages
		socket.addEventListener('message', (event: MessageEvent<any>) => {
			const jsonResponse: WebsocketData = JSON.parse(JSON.parse(event.data));
			const {item, message} = jsonResponse;
			websocketMsg = message;
			if (item == 'Ore') {
				console.log('Received Ore!')
				isOreTransfering = true;
				setTimeout(() => isOreTransfering = false, 1000);
			}

			if (item == 'Ingots') {
				console.log('Received Ingot!')
				isIngotTransfering = true;
				setTimeout(() => isIngotTransfering = false, 1000);
			}

			if (item == 'Pipes') {
				console.log('Received Pipe!')
				isPipeTransfering = true;
				setTimeout(() => isPipeTransfering = false, 1000);
			}
		});
	})
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Smelter" />
</svelte:head>

<section>
	<div class="container">
		<Miner />
		<ItemTransfer imageUrl='/iron_ore.png' shouldMove={isOreTransfering}/>
		<Smelter />
		<ItemTransfer imageUrl='/iron_ingot.png' shouldMove={isIngotTransfering}/>
		<Blacksmith />
		<ItemTransfer imageUrl='/pipe.png' shouldMove={isPipeTransfering}/>
		<Storage />
	</div>
	<h3>{websocketMsg}</h3>
</section>
<style>
	.container{
		display: flex;
		justify-content: center;
		align-items: center;
	}
</style>
