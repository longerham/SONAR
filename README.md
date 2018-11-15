SONAR - Software for Ontogenic aNalysis of Antibody Repertoires
=====

Introduction
-----

SONAR is the Antibodyomics2 pipeline developed collaboratively by the Structural Bioinformatics Section of the Vaccine Research Center, NIAID, NIH and the Shapiro lab at Columbia University. It is designed to process longitudinal NGS samples by extracting sequences related to a known antibody or antibodies of interest and reconstructing the ontogeny of the lineage. For more details, please see [below](#Using-SONAR). For examples of papers using SONAR, please see [here](#Papers).

If you use SONAR, please cite:
Schramm et al "SONAR: A High-Throughput Pipeline for Inferring Antibody Ontogenies from Longitudinal Sequencing of B Cell Transcripts." **Frontiers Immunol**, 2016. [PMCID: PMC5030719](https://www.frontiersin.org/articles/10.3389/fimmu.2016.00372/full)
For GSSPs, please cite:
Sheng et al "Gene-Specific Substitution Profiles Describe the Types and Frequencies of Amino Acid Changes during Antibody Somatic Hypermutation." **Frontiers Immunol**, 2017. [PMCID: PMC5424261](https://www.frontiersin.org/articles/10.3389/fimmu.2017.00537/full).

Installation
-----

**SONAR has now been update to Python3**

### Docker
SONAR is available as an automatically updated Docker image. To use Docker:
```
$> sudo docker pull scharch/sonar
$> sudo docker run -it -v ~:/host/home
$root@1abcde234> cd /host/home/*path*/*to*/*data*/
$root@1abcde234> sonar 1.1
.
.
.
```

### Installing locally

#### General Prerequisites:
* Python3 with Biopython, airr, and docopt
* Perl5 with BioPerl, Statistics::Basic, List::Util, and Algorithm::Combinatorics
* R with docopt ggplot2, MASS, and grid

#### Optional Prerequisites:
* For using the master script: fuzzywuzzy python package
* For displaying trees: ete3, PyQT4, and PyQt4.QtOpenGL python packages
* For comparing GSSPs: pandas python package

For details on how to install the prerequisites, follow the recipe used in the [Dockerfile](Dockerfile).

Then clone the github repo and run the setup utility:
```
$> git clone https://github.com/scharch/SONAR.git
$> cd sonar
$> ./setup.sh
```

For ease of use, you may wish to add the sonar directory to your PATH or to copy/link the `sonar` program file to, eg `~/bin`.

Using SONAR
-----


Change Log
-----
### New in version 3.0:
* SONAR now use Python3. Python2 is not supported.
* All Python scripts now use DocOpt to manage argument parsing. This means that most single dash options are now double dash options.
* Output is now in [AIRR format](https://www.frontiersin.org/articles/10.3389/fimmu.2018.02206/full). A 'rearrangements.tsv' file has replaced the old 'all_seq_stats.txt' file and several field names have changed. I've tried to maintain backward compatibility in most cases, but there is also a new `convertToAIRR.py` utility to help pull data over, if necessary.
* I've finally removed the double SONAR folder, which was never meant to be there in the first place. If you've added the SONAR module directories to your PATH, you'll need to update those references.
* `1.1_blastV.py` now includes an optional dereplication step, and will preserve replicate counts through the pipeline.
* `1.3_finalize_assignments` now distinguishes between `nonproductive` junctions and reads with other `indel`s.
* USearch has been replaced by VSearch, as the license of the latter allows me to include it in the SONAR distribution. In general, I've included most other programs that SONAR uses in the new `third_party/` folder, so that install is smoother and the user doesn't have to input paths to all sorts of things.
* In general, I've really tried to smooth out the install/setup process. Feedback welcome.
* IgPhyML replaces DNAML as the phylogenetic engine of choice. It is included in the `third_party/` folder.
* `1.4_dereplicate sequences.pl` has been replaced by `1.4_cluster_sequences.py` and `2.1-calculate_id-div.pl` has been replaced by `2.1-calculate_id-div.py`.
* The mGSSP pipeline has been reworked a little bit to allow for multithreading. It also now accomodates masking primer positions and building GSSPs from nonproductive repertoires. See [the mGSSP readme](mGSSP/mGSSP_readme.md) for more details.
* I added another FASTA extraction utility, `getReadsByAnnotation.py` to get more flexible subsets of reads. For instance, all reads assigned to IGHV1-2*02.

### New in version 2.0:
* Added a new mGSSP module. See [our paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5424261/) and [the mGSSP readme](mGSSP/mGSSP_readme.md) for more details.

Papers
-----
* Doria-Rose et al "Developmental pathway for potent V1V2-directed HIV-neutralizing antibodies." **Nature**, 2014. [PMCID: PMC4395007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4395007/)
* Wu et al "Maturation and Diversity of the VRC01-Antibody Lineage over 15 Years of Chronic HIV-1 Infection." **Cell** 2015. [PMCID: PMC4706178](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4706178/)
* Bhiman et al "Viral variants that initiate and drive maturation of V1V2-directed HIV-1 broadly neutralizing antibodies." **Nat Med**, 2015. [PMCID: PMC4637988](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4637988/)
* Doria-Rose et al "New Member of the V1V2-Directed CAP256-VRC26 Lineage That Shows Increased Breadth and Exceptional Potency." **J Virol**, 2016. [PMCID: PMC4702551](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4702551/)
* Sheng et al "Effects of Darwinian Selection and Mutability on Rate of Broadly Neutralizing Antibody Evolution during HIV-1 Infection." **PLoS Comput Biol**, 2016. [PMCID: PMC4871536](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4871536/)
* Huang et al "Identification of a CD4-Binding-Site Antibody to HIV that Evolved Near-Pan Neutralization Breadth." **Immunity**, 2016. [PMCID: PMC5770152](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5770152/) 
* Sheng et al "Gene-Specific Substitution Profiles Describe the Types and Frequencies of Amino Acid Changes during Antibody Somatic Hypermutation." **Frontiers Immunol**, 2017. [PMCID: PMC5424261](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5424261/)

