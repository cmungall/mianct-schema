# Auto generated from mianct.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-06-24 22:29
# Schema: mianct
#
# id: https://w3.org/mianct
# description: When should one provide an entry for a cell type in a MIANCT sheet? - When there is a claim of a
#              new cell class (type or state) that has not been described before - When new information is
#              discovered for a previously cataloged type that might influence its cataloguing (i.e. description
#              of the presence in a different species or in a new location) - When a cell type mentioned in the
#              article has been described before, but is not yet catalogued on an authoritative source like the
#              Cell Ontology.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
MESH = CurieNamespace('MESH', 'http://example.org/UNKNOWN/MESH/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIANCT = CurieNamespace('mianct', 'https://w3.org/mianct/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SDO = CurieNamespace('sdo', 'https://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MIANCT


# Types
class NarrativeText(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = MIANCT.NarrativeText


# Class references
class CellTypeId(extended_str):
    pass


class OrganismTaxonId(extended_str):
    pass


@dataclass
class CellType(YAMLRoot):
    """
    Minimal information about a cell type
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CL["0000000"]
    class_class_curie: ClassVar[str] = "CL:0000000"
    class_name: ClassVar[str] = "CellType"
    class_model_uri: ClassVar[URIRef] = MIANCT.CellType

    id: Union[str, CellTypeId] = None
    label: str = None
    organ_or_tissue: Optional[str] = None
    taxon: Optional[str] = None
    major_life_stage: Optional[Union[str, "MajorLifeStageEnum"]] = None
    major_class: Optional[Union[str, "MajorClassEnum"]] = None
    diagnostic_description: Optional[str] = None
    morphology: Optional[Union[str, "MorphologyEnum"]] = None
    develops_from: Optional[Union[str, CellTypeId]] = None
    develops_into: Optional[Union[Union[str, CellTypeId], List[Union[str, CellTypeId]]]] = empty_list()
    previous_observations: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeId):
            self.id = CellTypeId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.organ_or_tissue is not None and not isinstance(self.organ_or_tissue, str):
            self.organ_or_tissue = str(self.organ_or_tissue)

        if self.taxon is not None and not isinstance(self.taxon, str):
            self.taxon = str(self.taxon)

        if self.major_life_stage is not None and not isinstance(self.major_life_stage, MajorLifeStageEnum):
            self.major_life_stage = MajorLifeStageEnum(self.major_life_stage)

        if self.major_class is not None and not isinstance(self.major_class, MajorClassEnum):
            self.major_class = MajorClassEnum(self.major_class)

        if self.diagnostic_description is not None and not isinstance(self.diagnostic_description, str):
            self.diagnostic_description = str(self.diagnostic_description)

        if self.morphology is not None and not isinstance(self.morphology, MorphologyEnum):
            self.morphology = MorphologyEnum(self.morphology)

        if self.develops_from is not None and not isinstance(self.develops_from, CellTypeId):
            self.develops_from = CellTypeId(self.develops_from)

        if not isinstance(self.develops_into, list):
            self.develops_into = [self.develops_into] if self.develops_into is not None else []
        self.develops_into = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.develops_into]

        if not isinstance(self.previous_observations, list):
            self.previous_observations = [self.previous_observations] if self.previous_observations is not None else []
        self.previous_observations = [v if isinstance(v, str) else str(v) for v in self.previous_observations]

        super().__post_init__(**kwargs)


@dataclass
class OrganismTaxon(YAMLRoot):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria).
    Can also be used to represent strains or subspecies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.OrganismTaxon
    class_class_curie: ClassVar[str] = "biolink:OrganismTaxon"
    class_name: ClassVar[str] = "OrganismTaxon"
    class_model_uri: ClassVar[URIRef] = MIANCT.OrganismTaxon

    id: Union[str, OrganismTaxonId] = None
    label: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismTaxonId):
            self.id = OrganismTaxonId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


# Enumerations
class MajorClassEnum(EnumDefinitionImpl):

    neuron = PermissibleValue(text="neuron",
                                   meaning=CL["0000540"])
    leukocyte = PermissibleValue(text="leukocyte",
                                         meaning=CL["0000738"])
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="MajorClassEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "gial cell",
                PermissibleValue(text="gial cell",
                                 meaning=CL["0000125"]) )

class MajorLifeStageEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MajorLifeStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "post-embryonic",
                PermissibleValue(text="post-embryonic",
                                 meaning=UBERON["0000092"]) )
        setattr(cls, "embryonic or fetal",
                PermissibleValue(text="embryonic or fetal",
                                 meaning=UBERON["0000068"]) )
        setattr(cls, "larval stage",
                PermissibleValue(text="larval stage",
                                 meaning=UBERON["0000069"]) )

class MorphologyEnum(EnumDefinitionImpl):

    stellate = PermissibleValue(text="stellate")
    basket = PermissibleValue(text="basket")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="MorphologyEnum",
    )

# Slots

