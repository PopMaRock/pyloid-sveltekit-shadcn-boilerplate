import dns from "node:dns";
import { sveltekit } from "@sveltejs/kit/vite";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";

dns.setDefaultResultOrder("verbatim");
/** @type {import('vite').UserConfig} */
export default defineConfig({
	plugins: [
		sveltekit(
			/*{
			compilerOptions: { runes: true },
			onwarn: (warning, handler) => {
				// disable a11y warnings
				if (warning.code.startsWith("a11y-")) return;
				handler(warning);
			}
		}*/
		),
		tailwindcss()
	],
	ssr: {
		noExternal: ["pyloid-js"]
	},
	resolve: process.env.VITEST
		? {
				conditions: ["browser"]
			}
		: undefined,
	//ignore python virtual environment and src-pyloid folder
	server: {
		watch: {
			ignored: ["**/.venv/**", "**/src-pyloid/**"]
		}
	}
});