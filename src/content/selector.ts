export function selectRandomSource(sources: string[]): string | undefined {
  if (sources.length === 0){
    return undefined;
  }
  
  const randomIndex = Math.floor(Math.random() * sources.length);

  return sources[randomIndex]
}