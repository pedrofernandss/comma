import { selectRandomSource } from '@/content';

describe("Select Random Source", () => {
  it("Should select a valid source url from a given list", () => {
    const sources_url = [
      "website 01",
      "website 02",
      "website 03"
    ];

    const result = selectRandomSource(sources_url);
    expect(sources_url).toContain(result);
  });

  it('Should return undefined if the list is empty', () => {
    const sourceList: string[] = [];
    const selectedSource = selectRandomSource(sourceList);
    expect(selectedSource).toBeUndefined();
  });
});
