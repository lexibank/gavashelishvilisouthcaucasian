import pathlib
import attr
from clldutils.misc import slug
from pylexibank import Dataset as BaseDataset
from pylexibank import progressbar as pb
from pylexibank import Language
from pylexibank import FormSpec


@attr.s
class CustomLanguage(Language):
    Location = attr.ib(default=None)
    Remark = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "gavashelishvilisouthcaucasian"
    language_class = CustomLanguage
    form_spec = FormSpec(separators="~;,/", missing_data=["∅"], first_form_only=True)

    def cmd_download(self, args):
        self.raw_dir.download(
                "https://static-content.springer.com/esm/art%3A10.1038%2Fs41598-023-45500-w/MediaObjects/41598_2023_45500_MOESM3_ESM.xlsx",
                "data.xlsx"
                )

    def cmd_makecldf(self, args):
        pass
        # add bib
        #args.writer.add_sources()
        #args.log.info("added sources")

        ## add concept
        #concepts = args.writer.add_concepts(
        #    id_factory=lambda c: c.id.split("-")[-1] + "_" + slug(c.english),
        #    lookup_factory="Name",
        #)
        ## fix concept lookup
        #concepts["the barley (Tibetan or highland)"] = concepts[
        #    "the barley (tibetan or highland)"
        #]
        #concepts["to plant (vegetables, rice)"] = concepts["to plant (vegetals, rice)"]
        #args.log.info("added concepts")

        ## add language
        #languages = args.writer.add_languages(lookup_factory="Name")
        #args.log.info("added languages")

        ## read in data
        #data = self.raw_dir.read_csv(
        #    "Kusunda_2019_250_lexical_items.tsv", delimiter="\t", dicts=True
        #)
        ## add data
        #for entry in pb(data, desc="cldfify", total=len(data)):
        #    if entry["ENGLISH"] in concepts.keys():
        #        for key, val in languages.items():
        #            args.writer.add_forms_from_value(
        #                Language_ID=val,
        #                Parameter_ID=concepts[entry["ENGLISH"]],
        #                Value=entry[key],
        #                Source=["Bodt2019b"],
        #            )
