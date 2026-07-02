/** Estimate reading time (in minutes) for a Markdown string. */
export function readingTime(markdown: string | undefined): number {
	if (!markdown) return 1;
	const text = markdown
		.replace(/```[\s\S]*?```/g, ' ') // code blocks
		.replace(/!\[[^\]]*\]\([^)]*\)/g, ' ') // images
		.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1') // links → label
		.replace(/[#>*_`~-]/g, ' ');
	const words = text.split(/\s+/).filter(Boolean).length;
	return Math.max(1, Math.round(words / 220));
}
