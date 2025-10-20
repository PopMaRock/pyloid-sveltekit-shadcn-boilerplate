import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

export default {
	preprocess: vitePreprocess(),
	onwarn: (/** @type {{ code: string; }} */ warning, /** @type {(arg0: any) => void} */ handler) => {
		if (warning.code.startsWith("a11y-")) {
			return;
		}
		handler(warning);
	},
	compilerOptions: {
		customElement: false
	},
	kit: {
		adapter: adapter({
			out: "dist-front" //set dist folder to dist-front
		}),
		alias: {
			$components: "./src/components",
			$utilities: "./src/lib/utilities",
			$lib: "./src/lib",
		}
		// https://kit.svelte.dev/docs/configuration#alias
	}
};
