import spacy
from parser.TokenSpan import TokenSpan


print("Loading spacy")
nlp = spacy.load("en")
print("Done")


class TrainingExample():
    def __init__(self, sentence, answer, table):
        doc = nlp(sentence)

        tokens = []
        espans = []
        nspans = []
        ne_start = -1
        for t in range(len(doc)):
            tokens.append(doc[t].text)
            if doc[t].ent_iob == 3:
                if ne_start >= 0:
                    if str(doc[ne_start].ent_type_) in entity_types:
                        espans.append((ne_start, t))
                    elif str(doc[ne_start].ent_type_) in atomic_types:
                        nspans.append((ne_start, t))
                else:
                    ne_start = t
            elif doc[t].ent_iob == 2:
                if ne_start >= 0:
                    if str(doc[ne_start].ent_type_) in entity_types:
                        espans.append((ne_start, t))
                    elif str(doc[ne_start].ent_type_) in atomic_types:
                        nspans.append((ne_start, t))
                    ne_start = -1

        token_spans = []
        for espan in espans:
            start = espan[0]
            end = espan[1]

            ts = TokenSpan(tokens, start, end)
            token_spans.append(ts)

        self.nes = token_spans
        token_spans = []
        for espan in nspans:
            start = espan[0]
            end = espan[1]

            ts = TokenSpan(tokens, start, end)
            token_spans.append(ts)

        self.words = tokens
        self.answer = answer
        self.table = table
        self.nums = token_spans


if __name__ == "__main__":
    ex = TrainingExample("Greece last held its summer olympics in which year? There are 100 types of fish. The exam is on 3rd September 2005.","2004","test.tsv")
    print(ex.words)
    print(ex.nes)