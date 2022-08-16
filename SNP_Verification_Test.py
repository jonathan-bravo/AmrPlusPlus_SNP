#   AMRPlusPlus_SNP_Verification
#   Copyright (C) 2022  Nathalie Bonin
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see https://www.gnu.org/licenses/.

from SNP_Verification_Tools.Gene import Gene
from SNP_Verification_Tools.SNP import SNP
from SNP_Verification_Tools import dnaTranslate
from SNP_Verification_Tools import reverseTranslation

header = """@HD	VN:1.6	SO:coordinate
@SQ	SN:MEG_1|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1507
@SQ	SN:MEG_2|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1544
@SQ	SN:MEG_3|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1537
@SQ	SN:MEG_4|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1551
@SQ	SN:MEG_5|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1504
@SQ	SN:MEG_6|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1551
@SQ	SN:MEG_7|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1544
@SQ	SN:MEG_8|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1474
@SQ	SN:MEG_9|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1528
@SQ	SN:MEG_10|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1477
@SQ	SN:MEG_11|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1441
@SQ	SN:MEG_12|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|A16S|RequiresSNPConfirmation	LN:1454
@SQ	SN:MEG_411|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|ACRR|RequiresSNPConfirmation	LN:648
@SQ	SN:MEG_412|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|ACRR|RequiresSNPConfirmation	LN:540
@SQ	SN:MEG_413|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|ACRR|RequiresSNPConfirmation	LN:651
@SQ	SN:MEG_414|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|ACRR|RequiresSNPConfirmation	LN:651
@SQ	SN:MEG_1187|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_pumps|AXYZ|RequiresSNPConfirmation	LN:639
@SQ	SN:MEG_1197|Drugs|Cationic_antimicrobial_peptides|Polymyxin_B_resistance_regulator|BASRS|RequiresSNPConfirmation	LN:666
@SQ	SN:MEG_1490|Drugs|Cationic_antimicrobial_peptides|Cationic_peptide-resistant_16S_ribosomal_subunit_protein|CAP16S|RequiresSNPConfirmation	LN:1542
@SQ	SN:MEG_1594|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1595|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1596|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1597|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1598|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1599|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1600|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1601|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1602|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1603|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1604|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1605|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1606|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1607|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:1260
@SQ	SN:MEG_1608|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1609|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1610|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1611|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1612|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1613|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1614|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1615|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1616|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1617|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1618|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1619|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1620|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:549
@SQ	SN:MEG_1621|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:630
@SQ	SN:MEG_1622|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:630
@SQ	SN:MEG_1623|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1624|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1625|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1626|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1627|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1628|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:630
@SQ	SN:MEG_1629|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1630|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATB|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_1631|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATP|RequiresSNPConfirmation	LN:639
@SQ	SN:MEG_1632|Drugs|Phenicol|Chloramphenicol_acetyltransferases|CATP|RequiresSNPConfirmation	LN:624
@SQ	SN:MEG_1642|Drugs|Lipopeptides|Daptomycin-resistant_mutant|CDSA|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_1730|Drugs|Lipopeptides|Daptomycin-resistant_mutant|CLS|RequiresSNPConfirmation	LN:1485
@SQ	SN:MEG_1731|Drugs|Lipopeptides|Daptomycin-resistant_mutant|CLS|RequiresSNPConfirmation	LN:1446
@SQ	SN:MEG_1732|Drugs|Lipopeptides|Daptomycin-resistant_mutant|CLS|RequiresSNPConfirmation	LN:1452
@SQ	SN:MEG_2572|Drugs|Trimethoprim|Dihydrofolate_reductase|DFRC|RequiresSNPConfirmation	LN:486
@SQ	SN:MEG_2573|Drugs|Trimethoprim|Dihydrofolate_reductase|DFRC|RequiresSNPConfirmation	LN:486
@SQ	SN:MEG_2615|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2616|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:498
@SQ	SN:MEG_2617|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:561
@SQ	SN:MEG_2618|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2619|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2620|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:459
@SQ	SN:MEG_2621|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2622|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:472
@SQ	SN:MEG_2623|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2624|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2625|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2626|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:510
@SQ	SN:MEG_2627|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:558
@SQ	SN:MEG_2628|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2629|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:459
@SQ	SN:MEG_2630|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:483
@SQ	SN:MEG_2631|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:498
@SQ	SN:MEG_2632|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2633|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2634|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:498
@SQ	SN:MEG_2635|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2636|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:570
@SQ	SN:MEG_2637|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2638|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:606
@SQ	SN:MEG_2639|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2640|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2641|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:522
@SQ	SN:MEG_2642|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2643|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2644|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:483
@SQ	SN:MEG_2645|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2646|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFR|RequiresSNPConfirmation	LN:474
@SQ	SN:MEG_2647|Drugs|Trimethoprim|Dihydrofolate_reductase|DHFRIII|RequiresSNPConfirmation	LN:489
@SQ	SN:MEG_2693|Drugs|Multi-drug_resistance|Multi-drug_ABC_efflux_pumps|EATAV|RequiresSNPConfirmation	LN:1503
@SQ	SN:MEG_2694|Drugs|Multi-drug_resistance|Multi-drug_ABC_efflux_pumps|EATAV|RequiresSNPConfirmation	LN:1503
@SQ	SN:MEG_2709|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol_resistant_arabinosyltransferase|EMBA|RequiresSNPConfirmation	LN:3285
@SQ	SN:MEG_2710|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol_resistant_arabinosyltransferase|EMBB|RequiresSNPConfirmation	LN:3297
@SQ	SN:MEG_2711|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol_resistant_arabinosyltransferase|EMBB|RequiresSNPConfirmation	LN:3297
@SQ	SN:MEG_2712|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol_resistant_arabinosyltransferase|EMBC|RequiresSNPConfirmation	LN:3285
@SQ	SN:MEG_2713|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol_resistant_arabinosyltransferase|EMBR|RequiresSNPConfirmation	LN:1167
@SQ	SN:MEG_2866|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethionamide-resistant_mutant|ETHA|RequiresSNPConfirmation	LN:1470
@SQ	SN:MEG_2873|Biocides|Phenolic_compound_resistance|Triclosan-resistant_mutation|FABG|RequiresSNPConfirmation	LN:735
@SQ	SN:MEG_2933|Drugs|Mycobacterium_tuberculosis-specific_Drug|Para-aminosalicylic_acid_resistant_mutant|FOLC|RequiresSNPConfirmation	LN:1464
@SQ	SN:MEG_2934|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:801
@SQ	SN:MEG_2935|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:855
@SQ	SN:MEG_2936|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:822
@SQ	SN:MEG_2937|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:1143
@SQ	SN:MEG_2938|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:852
@SQ	SN:MEG_2939|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:843
@SQ	SN:MEG_2940|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:1188
@SQ	SN:MEG_2941|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:912
@SQ	SN:MEG_2942|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:792
@SQ	SN:MEG_2943|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:876
@SQ	SN:MEG_2944|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:885
@SQ	SN:MEG_2945|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2946|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:843
@SQ	SN:MEG_2947|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:795
@SQ	SN:MEG_2948|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:849
@SQ	SN:MEG_2949|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2950|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2951|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2952|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:849
@SQ	SN:MEG_2953|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:858
@SQ	SN:MEG_2954|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:840
@SQ	SN:MEG_2955|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:894
@SQ	SN:MEG_2956|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2957|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:978
@SQ	SN:MEG_2958|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:852
@SQ	SN:MEG_2959|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:849
@SQ	SN:MEG_2960|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:1143
@SQ	SN:MEG_2961|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:852
@SQ	SN:MEG_2962|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2963|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2964|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:927
@SQ	SN:MEG_2965|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:843
@SQ	SN:MEG_2966|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:849
@SQ	SN:MEG_2967|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:858
@SQ	SN:MEG_2968|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:804
@SQ	SN:MEG_2969|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:957
@SQ	SN:MEG_2970|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:819
@SQ	SN:MEG_2971|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:843
@SQ	SN:MEG_2972|Drugs|Sulfonamides|Sulfonamide-resistant_dihydropteroate_synthases|FOLP|RequiresSNPConfirmation	LN:849
@SQ	SN:MEG_3065|Drugs|Fusidic_acid|Fusidic_acid-resistant_mutation|FUSA|RequiresSNPConfirmation	LN:2082
@SQ	SN:MEG_3071|Drugs|Fusidic_acid|Fusidic_acid-resistant_mutation|FUSE|RequiresSNPConfirmation	LN:537
@SQ	SN:MEG_3135|Drugs|Aminoglycosides|Aminoglycoside-resistant_gidB|GIDB|RequiresSNPConfirmation	LN:675
@SQ	SN:MEG_3143|Drugs|Fosfomycin|Fosfomycin_target_mutation|GLPT|RequiresSNPConfirmation	LN:1359
@SQ	SN:MEG_3144|Drugs|Fosfomycin|Fosfomycin_target_mutation|GLPT|RequiresSNPConfirmation	LN:1359
@SQ	SN:MEG_3175|Drugs|Lipopeptides|Daptomycin-resistant_mutant|GSHF|RequiresSNPConfirmation	LN:2271
@SQ	SN:MEG_3176|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2511
@SQ	SN:MEG_3177|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2751
@SQ	SN:MEG_3178|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2628
@SQ	SN:MEG_3179|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2787
@SQ	SN:MEG_3180|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2517
@SQ	SN:MEG_3181|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:3750
@SQ	SN:MEG_3182|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2676
@SQ	SN:MEG_3183|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2715
@SQ	SN:MEG_3184|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2646
@SQ	SN:MEG_3185|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2511
@SQ	SN:MEG_3186|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2661
@SQ	SN:MEG_3187|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2628
@SQ	SN:MEG_3188|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2634
@SQ	SN:MEG_3189|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2634
@SQ	SN:MEG_3190|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2589
@SQ	SN:MEG_3191|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2670
@SQ	SN:MEG_3192|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2715
@SQ	SN:MEG_3193|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2715
@SQ	SN:MEG_3194|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2751
@SQ	SN:MEG_3195|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2535
@SQ	SN:MEG_3196|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2541
@SQ	SN:MEG_3197|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2442
@SQ	SN:MEG_3198|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2469
@SQ	SN:MEG_3199|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2682
@SQ	SN:MEG_3200|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2502
@SQ	SN:MEG_3201|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2637
@SQ	SN:MEG_3202|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2592
@SQ	SN:MEG_3203|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2643
@SQ	SN:MEG_3204|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2487
@SQ	SN:MEG_3205|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2637
@SQ	SN:MEG_3206|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2595
@SQ	SN:MEG_3207|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2664
@SQ	SN:MEG_3208|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2634
@SQ	SN:MEG_3209|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2592
@SQ	SN:MEG_3210|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2424
@SQ	SN:MEG_3211|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2382
@SQ	SN:MEG_3212|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2628
@SQ	SN:MEG_3213|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2493
@SQ	SN:MEG_3214|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2529
@SQ	SN:MEG_3215|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2715
@SQ	SN:MEG_3216|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2685
@SQ	SN:MEG_3217|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2751
@SQ	SN:MEG_3218|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2592
@SQ	SN:MEG_3219|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2427
@SQ	SN:MEG_3220|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2637
@SQ	SN:MEG_3221|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2661
@SQ	SN:MEG_3222|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2664
@SQ	SN:MEG_3223|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2664
@SQ	SN:MEG_3224|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2676
@SQ	SN:MEG_3225|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2469
@SQ	SN:MEG_3226|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2772
@SQ	SN:MEG_3227|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2628
@SQ	SN:MEG_3228|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2715
@SQ	SN:MEG_3229|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2682
@SQ	SN:MEG_3230|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2664
@SQ	SN:MEG_3231|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2682
@SQ	SN:MEG_3232|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2715
@SQ	SN:MEG_3233|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2670
@SQ	SN:MEG_3234|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2637
@SQ	SN:MEG_3235|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2466
@SQ	SN:MEG_3236|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2670
@SQ	SN:MEG_3237|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRA|RequiresSNPConfirmation	LN:2517
@SQ	SN:MEG_3238|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRB|RequiresSNPConfirmation	LN:2415
@SQ	SN:MEG_3239|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRB|RequiresSNPConfirmation	LN:2037
@SQ	SN:MEG_3240|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRB|RequiresSNPConfirmation	LN:1953
@SQ	SN:MEG_3241|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRB|RequiresSNPConfirmation	LN:1914
@SQ	SN:MEG_3242|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRB|RequiresSNPConfirmation	LN:2415
@SQ	SN:MEG_3243|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRB|RequiresSNPConfirmation	LN:2028
@SQ	SN:MEG_3244|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|GYRBA|RequiresSNPConfirmation	LN:2415
@SQ	SN:MEG_3245|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|GYRBA|RequiresSNPConfirmation	LN:1932
@SQ	SN:MEG_3246|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|GYRBA|RequiresSNPConfirmation	LN:2430
@SQ	SN:MEG_3247|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|GYRBA|RequiresSNPConfirmation	LN:1718
@SQ	SN:MEG_3248|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|GYRBA|RequiresSNPConfirmation	LN:2034
@SQ	SN:MEG_3249|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|GYRBA|RequiresSNPConfirmation	LN:2034
@SQ	SN:MEG_3250|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|GYRBA|RequiresSNPConfirmation	LN:2034
@SQ	SN:MEG_3251|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|GYRC|RequiresSNPConfirmation	LN:2256
@SQ	SN:MEG_3296|Drugs|Mupirocin|Mupirocin-resistant_isoleucyl-tRNA_synthetase|ILES|RequiresSNPConfirmation	LN:2754
@SQ	SN:MEG_3429|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|INHA|RequiresSNPConfirmation	LN:810
@SQ	SN:MEG_3430|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol-resistant_mutant|INIA|RequiresSNPConfirmation	LN:1923
@SQ	SN:MEG_3431|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol-resistant_mutant|INIB|RequiresSNPConfirmation	LN:1440
@SQ	SN:MEG_3432|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethambutol-resistant_mutant|INIC|RequiresSNPConfirmation	LN:1482
@SQ	SN:MEG_3445|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|KASA|RequiresSNPConfirmation	LN:1251
@SQ	SN:MEG_3446|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|KATG|RequiresSNPConfirmation	LN:2223
@SQ	SN:MEG_3586|Drugs|Lipopeptides|Daptomycin-resistant_mutant|LIAFSR|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_3587|Drugs|Lipopeptides|Daptomycin-resistant_mutant|LIAFSR|RequiresSNPConfirmation	LN:1104
@SQ	SN:MEG_3588|Drugs|Lipopeptides|Daptomycin-resistant_mutant|LIAFSR|RequiresSNPConfirmation	LN:732
@SQ	SN:MEG_3589|Drugs|Lipopeptides|Daptomycin-resistant_mutant|LIAFSR|RequiresSNPConfirmation	LN:1068
@SQ	SN:MEG_3590|Drugs|Lipopeptides|Daptomycin-resistant_mutant|LIAFSR|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_3591|Drugs|Lipopeptides|Daptomycin-resistant_mutant|LIAFSR|RequiresSNPConfirmation	LN:732
@SQ	SN:MEG_3594|Drugs|Multi-drug_resistance|Multi-drug_ABC_efflux_pumps|LMRA|RequiresSNPConfirmation	LN:1446
@SQ	SN:MEG_3626|Drugs|Lipopeptides|Colistin-resistant_mutant|LPXA|RequiresSNPConfirmation	LN:789
@SQ	SN:MEG_3627|Drugs|Lipopeptides|Colistin-resistant_mutant|LPXC|RequiresSNPConfirmation	LN:903
@SQ	SN:MEG_3740|Drugs|Multi-drug_resistance|MDR_23S_rRNA_mutation|MDR23S|RequiresSNPConfirmation	LN:2734
@SQ	SN:MEG_3831|Drugs|Lipopeptides|Lysocin-resistant_mutant|MENA|RequiresSNPConfirmation	LN:939
@SQ	SN:MEG_3931|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|MEXS|RequiresSNPConfirmation	LN:1020
@SQ	SN:MEG_3932|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|MEXT|RequiresSNPConfirmation	LN:915
@SQ	SN:MEG_3933|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|MEXT|RequiresSNPConfirmation	LN:1044
@SQ	SN:MEG_3941|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|MEXZ|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_3975|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3162
@SQ	SN:MEG_3976|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2975
@SQ	SN:MEG_3977|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2904
@SQ	SN:MEG_3978|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3156
@SQ	SN:MEG_3979|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2884
@SQ	SN:MEG_3980|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3113
@SQ	SN:MEG_3981|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3403
@SQ	SN:MEG_3982|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3112
@SQ	SN:MEG_3983|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2886
@SQ	SN:MEG_3984|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3112
@SQ	SN:MEG_3985|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3103
@SQ	SN:MEG_3986|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2940
@SQ	SN:MEG_3987|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2912
@SQ	SN:MEG_3988|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2900
@SQ	SN:MEG_3989|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2905
@SQ	SN:MEG_3990|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3149
@SQ	SN:MEG_3991|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2996
@SQ	SN:MEG_3992|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:2904
@SQ	SN:MEG_3993|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3118
@SQ	SN:MEG_3994|Drugs|MLS|Macrolide-resistant_23S_rRNA_mutation|MLS23S|RequiresSNPConfirmation	LN:3135
@SQ	SN:MEG_4057|Drugs|Lipopeptides|Daptomycin-resistant_mutant|MPRFD|RequiresSNPConfirmation	LN:2511
@SQ	SN:MEG_4087|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_MFS_efflux_regulator|MTRR|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_4088|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_MFS_efflux_regulator|MTRR|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_4092|Drugs|Fosfomycin|Fosfomycin_target_mutation|MURA|RequiresSNPConfirmation	LN:1284
@SQ	SN:MEG_4093|Drugs|Fosfomycin|Fosfomycin_target_mutation|MURA|RequiresSNPConfirmation	LN:1335
@SQ	SN:MEG_4094|Drugs|Fosfomycin|Fosfomycin_target_mutation|MURA|RequiresSNPConfirmation	LN:1266
@SQ	SN:MEG_4095|Drugs|Fosfomycin|Fosfomycin_target_mutation|MURA|RequiresSNPConfirmation	LN:1260
@SQ	SN:MEG_4096|Drugs|Fosfomycin|Fosfomycin_target_mutation|MURA|RequiresSNPConfirmation	LN:1257
@SQ	SN:MEG_4097|Drugs|Glycopeptides|Vancomycin-resistant_mutation|MURG|RequiresSNPConfirmation	LN:1080
@SQ	SN:MEG_4109|Drugs|Multi-drug_resistance|Multi-drug_RND_efflux_pumps|NALC|RequiresSNPConfirmation	LN:642
@SQ	SN:MEG_4110|Drugs|Multi-drug_resistance|Multi-drug_RND_efflux_regulator|NALD|RequiresSNPConfirmation	LN:639
@SQ	SN:MEG_4130|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|NDH|RequiresSNPConfirmation	LN:1392
@SQ	SN:MEG_4131|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|NDH|RequiresSNPConfirmation	LN:1392
@SQ	SN:MEG_4132|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|NDH|RequiresSNPConfirmation	LN:1374
@SQ	SN:MEG_4161|Drugs|Multi-drug_resistance|Multi-drug_RND_efflux_pumps|NFXB|RequiresSNPConfirmation	LN:564
@SQ	SN:MEG_4223|Drugs|Oxazolidinone|Oxazolidinone-resistant_23S_rRNA_mutation|O23S|RequiresSNPConfirmation	LN:2926
@SQ	SN:MEG_4279|Drugs|betalactams|Mutant_porin_proteins|OMP36|RequiresSNPConfirmation	LN:1128
@SQ	SN:MEG_4280|Drugs|betalactams|Mutant_porin_proteins|OMP36|RequiresSNPConfirmation	LN:1131
@SQ	SN:MEG_4281|Drugs|betalactams|Mutant_porin_proteins|OMP36|RequiresSNPConfirmation	LN:1128
@SQ	SN:MEG_4282|Drugs|betalactams|Mutant_porin_proteins|OMP36|RequiresSNPConfirmation	LN:1128
@SQ	SN:MEG_4286|Drugs|Multi-drug_resistance|MDR_mutant_porin_proteins|OMPF|RequiresSNPConfirmation	LN:927
@SQ	SN:MEG_4287|Drugs|Multi-drug_resistance|MDR_mutant_porin_proteins|OMPF|RequiresSNPConfirmation	LN:1098
@SQ	SN:MEG_4288|Drugs|Multi-drug_resistance|MDR_mutant_porin_proteins|OMPF|RequiresSNPConfirmation	LN:1092
@SQ	SN:MEG_4289|Drugs|betalactams|Mutant_porin_proteins|OMPFB|RequiresSNPConfirmation	LN:1089
@SQ	SN:MEG_4296|Drugs|betalactams|Mutant_porin_proteins|OPRD|RequiresSNPConfirmation	LN:1332
@SQ	SN:MEG_5322|Drugs|Pactamycin|Pactamycin-resistant_16S_ribosomal_subunit_protein|P16S|RequiresSNPConfirmation	LN:1473
@SQ	SN:MEG_5323|Drugs|Pleuromutilin|Pleuromutilin-resistant_23S_rRNA_mutation|P23S|RequiresSNPConfirmation	LN:2913
@SQ	SN:MEG_5325|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2265
@SQ	SN:MEG_5326|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2304
@SQ	SN:MEG_5327|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2472
@SQ	SN:MEG_5328|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2553
@SQ	SN:MEG_5329|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2403
@SQ	SN:MEG_5330|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2802
@SQ	SN:MEG_5331|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2346
@SQ	SN:MEG_5332|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2259
@SQ	SN:MEG_5333|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2259
@SQ	SN:MEG_5334|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2259
@SQ	SN:MEG_5335|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2220
@SQ	SN:MEG_5336|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2220
@SQ	SN:MEG_5337|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2256
@SQ	SN:MEG_5338|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2544
@SQ	SN:MEG_5339|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2871
@SQ	SN:MEG_5340|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2481
@SQ	SN:MEG_5341|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2463
@SQ	SN:MEG_5342|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2271
@SQ	SN:MEG_5343|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2451
@SQ	SN:MEG_5344|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2403
@SQ	SN:MEG_5345|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2403
@SQ	SN:MEG_5346|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2958
@SQ	SN:MEG_5347|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2256
@SQ	SN:MEG_5348|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2259
@SQ	SN:MEG_5349|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2424
@SQ	SN:MEG_5350|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2220
@SQ	SN:MEG_5351|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2304
@SQ	SN:MEG_5352|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2220
@SQ	SN:MEG_5353|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2259
@SQ	SN:MEG_5354|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2403
@SQ	SN:MEG_5355|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2403
@SQ	SN:MEG_5356|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2481
@SQ	SN:MEG_5357|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2265
@SQ	SN:MEG_5358|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2220
@SQ	SN:MEG_5359|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2403
@SQ	SN:MEG_5360|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2316
@SQ	SN:MEG_5361|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2259
@SQ	SN:MEG_5362|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2403
@SQ	SN:MEG_5363|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation	LN:2193
@SQ	SN:MEG_5364|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1974
@SQ	SN:MEG_5365|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1896
@SQ	SN:MEG_5366|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1998
@SQ	SN:MEG_5367|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1884
@SQ	SN:MEG_5368|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1887
@SQ	SN:MEG_5369|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1881
@SQ	SN:MEG_5370|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1971
@SQ	SN:MEG_5371|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1956
@SQ	SN:MEG_5372|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1944
@SQ	SN:MEG_5373|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:2058
@SQ	SN:MEG_5374|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1893
@SQ	SN:MEG_5375|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1896
@SQ	SN:MEG_5376|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1881
@SQ	SN:MEG_5377|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1968
@SQ	SN:MEG_5378|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1971
@SQ	SN:MEG_5379|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1998
@SQ	SN:MEG_5380|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1986
@SQ	SN:MEG_5381|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1893
@SQ	SN:MEG_5382|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1893
@SQ	SN:MEG_5383|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1998
@SQ	SN:MEG_5384|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1998
@SQ	SN:MEG_5385|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1944
@SQ	SN:MEG_5386|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1890
@SQ	SN:MEG_5387|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1998
@SQ	SN:MEG_5388|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1884
@SQ	SN:MEG_5389|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1962
@SQ	SN:MEG_5390|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1998
@SQ	SN:MEG_5391|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1992
@SQ	SN:MEG_5392|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:2079
@SQ	SN:MEG_5393|Drugs|Aminocoumarins|Aminocoumarin-resistant_DNA_topoisomerases|PARE|RequiresSNPConfirmation	LN:1893
@SQ	SN:MEG_5394|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PAREF|RequiresSNPConfirmation	LN:1893
@SQ	SN:MEG_5395|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PAREF|RequiresSNPConfirmation	LN:1998
@SQ	SN:MEG_5399|Drugs|betalactams|Penicillin_binding_protein|PBP1A|RequiresSNPConfirmation	LN:2160
@SQ	SN:MEG_5401|Drugs|betalactams|Penicillin_binding_protein|PBP2|RequiresSNPConfirmation	LN:1746
@SQ	SN:MEG_5405|Drugs|betalactams|Penicillin_binding_protein|PBP2|RequiresSNPConfirmation	LN:1746
@SQ	SN:MEG_5406|Drugs|betalactams|Penicillin_binding_protein|PBP2B|RequiresSNPConfirmation	LN:2058
@SQ	SN:MEG_5407|Drugs|betalactams|Penicillin_binding_protein|PBP2X|RequiresSNPConfirmation	LN:2253
@SQ	SN:MEG_5408|Drugs|betalactams|Penicillin_binding_protein|PBP3|RequiresSNPConfirmation	LN:1833
@SQ	SN:MEG_5779|Drugs|Lipopeptides|Daptomycin-resistant_mutant|PGSA|RequiresSNPConfirmation	LN:1143
@SQ	SN:MEG_5780|Drugs|Lipopeptides|Daptomycin-resistant_mutant|PGSA|RequiresSNPConfirmation	LN:579
@SQ	SN:MEG_5781|Drugs|Phenicol|Phenicol-resistant_23S_rRNA_mutation|PH23S|RequiresSNPConfirmation	LN:2905
@SQ	SN:MEG_5782|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_ABC_efflux_regulator|PHOB|RequiresSNPConfirmation	LN:714
@SQ	SN:MEG_5783|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_ABC_efflux_regulator|PHOB|RequiresSNPConfirmation	LN:672
@SQ	SN:MEG_5784|Drugs|Lipopeptides|Colistin-resistant_mutant|PHOP|RequiresSNPConfirmation	LN:678
@SQ	SN:MEG_5785|Drugs|Lipopeptides|Colistin-resistant_mutant|PHOQ|RequiresSNPConfirmation	LN:1347
@SQ	SN:MEG_5803|Drugs|Mycobacterium_tuberculosis-specific_Drug|Pyrazinamide-resistant_mutant|PNCA|RequiresSNPConfirmation	LN:561
@SQ	SN:MEG_5808|Drugs|Multi-drug_resistance|MDR_mutant_porin_proteins|POR|RequiresSNPConfirmation	LN:1047
@SQ	SN:MEG_5819|Drugs|Fosfomycin|Fosfomycin_target_mutation|PTSL|RequiresSNPConfirmation	LN:1728
@SQ	SN:MEG_6045|Drugs|Multi-drug_resistance|Multi-drug_RND_efflux_regulator|RAMR|RequiresSNPConfirmation	LN:582
@SQ	SN:MEG_6046|Drugs|Multi-drug_resistance|Multi-drug_RND_efflux_regulator|RAMR|RequiresSNPConfirmation	LN:582
@SQ	SN:MEG_6055|Drugs|Mycobacterium_tuberculosis-specific_Drug|Para-aminosalicylic_acid_resistant_mutant|RIBD|RequiresSNPConfirmation	LN:777
@SQ	SN:MEG_6090|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3519
@SQ	SN:MEG_6091|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3537
@SQ	SN:MEG_6092|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3489
@SQ	SN:MEG_6093|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3498
@SQ	SN:MEG_6094|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4029
@SQ	SN:MEG_6095|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3729
@SQ	SN:MEG_6096|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4134
@SQ	SN:MEG_6097|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4011
@SQ	SN:MEG_6098|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6099|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4062
@SQ	SN:MEG_6100|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4089
@SQ	SN:MEG_6101|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4107
@SQ	SN:MEG_6102|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3540
@SQ	SN:MEG_6103|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3699
@SQ	SN:MEG_6104|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4110
@SQ	SN:MEG_6105|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3651
@SQ	SN:MEG_6106|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3624
@SQ	SN:MEG_6107|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4029
@SQ	SN:MEG_6108|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4071
@SQ	SN:MEG_6109|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4185
@SQ	SN:MEG_6110|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6111|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6112|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6113|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4029
@SQ	SN:MEG_6114|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4107
@SQ	SN:MEG_6115|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3591
@SQ	SN:MEG_6116|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3543
@SQ	SN:MEG_6117|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6118|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3627
@SQ	SN:MEG_6119|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4137
@SQ	SN:MEG_6120|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3717
@SQ	SN:MEG_6121|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4089
@SQ	SN:MEG_6122|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4029
@SQ	SN:MEG_6123|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4029
@SQ	SN:MEG_6124|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6125|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4179
@SQ	SN:MEG_6126|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3612
@SQ	SN:MEG_6127|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4074
@SQ	SN:MEG_6128|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6129|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4113
@SQ	SN:MEG_6130|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4029
@SQ	SN:MEG_6131|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4089
@SQ	SN:MEG_6132|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3582
@SQ	SN:MEG_6133|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6134|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:3537
@SQ	SN:MEG_6135|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation	LN:4029
@SQ	SN:MEG_6136|Drugs|Lipopeptides|Daptomycin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOBL|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6137|Drugs|Lipopeptides|Daptomycin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOBL|RequiresSNPConfirmation	LN:3552
@SQ	SN:MEG_6138|Drugs|Glycopeptides|Vancomycin-resistant_mutation|RPOC|RequiresSNPConfirmation	LN:3486
@SQ	SN:MEG_6139|Drugs|Lipopeptides|Daptomycin-resistant_beta-subunit_of_RNA_polymerase_RpoC|RPOCL|RequiresSNPConfirmation	LN:3624
@SQ	SN:MEG_6142|Drugs|Mycobacterium_tuberculosis-specific_Drug|Pyrazinamide-resistant_mutant|RPSA|RequiresSNPConfirmation	LN:1446
@SQ	SN:MEG_6143|Drugs|Tetracyclines|Tetracycline_resistance_ribosomal_protection_proteins|RPSJ|RequiresSNPConfirmation	LN:312
@SQ	SN:MEG_6144|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|RPSL|RequiresSNPConfirmation	LN:375
@SQ	SN:MEG_6145|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|RRSA|RequiresSNPConfirmation	LN:1529
@SQ	SN:MEG_6146|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|RRSC|RequiresSNPConfirmation	LN:1542
@SQ	SN:MEG_6147|Drugs|Aminoglycosides|Aminoglycoside-resistant_16S_ribosomal_subunit_protein|RRSH|RequiresSNPConfirmation	LN:1542
@SQ	SN:MEG_6548|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_ABC_efflux_regulator|SOXR|RequiresSNPConfirmation	LN:459
@SQ	SN:MEG_6552|Multi-compound|Drug_and_biocide_and_metal_resistance|Drug_and_biocide_and_metal_resistance_regulator|SOXS|RequiresSNPConfirmation	LN:324
@SQ	SN:MEG_6963|Drugs|Tetracyclines|Tetracycline-resistant_16S_ribosomal_subunit_protein|TET16S|RequiresSNPConfirmation	LN:1501
@SQ	SN:MEG_6964|Drugs|Tetracyclines|Tetracycline-resistant_16S_ribosomal_subunit_protein|TET16S|RequiresSNPConfirmation	LN:1486
@SQ	SN:MEG_7185|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:651
@SQ	SN:MEG_7186|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:633
@SQ	SN:MEG_7187|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:642
@SQ	SN:MEG_7188|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:648
@SQ	SN:MEG_7189|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:612
@SQ	SN:MEG_7190|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:615
@SQ	SN:MEG_7191|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:600
@SQ	SN:MEG_7192|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:732
@SQ	SN:MEG_7193|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:627
@SQ	SN:MEG_7194|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:624
@SQ	SN:MEG_7195|Drugs|Tetracyclines|Tetracycline_transcriptional_repressor|TETR|RequiresSNPConfirmation	LN:642
@SQ	SN:MEG_7196|Drugs|Tetracyclines|Tetracycline_resistance_MFS_efflux_regulator|TETRM|RequiresSNPConfirmation	LN:627
@SQ	SN:MEG_7197|Drugs|Tetracyclines|Tetracycline_resistance_MFS_efflux_regulator|TETRM|RequiresSNPConfirmation	LN:567
@SQ	SN:MEG_7250|Drugs|Mycobacterium_tuberculosis-specific_Drug|Para-aminosalicylic_acid_resistant_mutant|THYA|RequiresSNPConfirmation	LN:792
@SQ	SN:MEG_7258|Drugs|Aminoglycosides|Aminoglycoside-resistant_arabinosyltransferase|TLYA|RequiresSNPConfirmation	LN:807
@SQ	SN:MEG_7259|Drugs|Aminoglycosides|Aminoglycoside-resistant_arabinosyltransferase|TLYA|RequiresSNPConfirmation	LN:3297
@SQ	SN:MEG_7301|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1230
@SQ	SN:MEG_7302|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7303|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1272
@SQ	SN:MEG_7304|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1194
@SQ	SN:MEG_7305|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1194
@SQ	SN:MEG_7306|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1194
@SQ	SN:MEG_7307|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:705
@SQ	SN:MEG_7308|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1191
@SQ	SN:MEG_7309|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:924
@SQ	SN:MEG_7310|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7311|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1200
@SQ	SN:MEG_7312|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7313|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7314|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1194
@SQ	SN:MEG_7315|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7316|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1236
@SQ	SN:MEG_7317|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7318|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1188
@SQ	SN:MEG_7319|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7320|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1194
@SQ	SN:MEG_7321|Drugs|Elfamycins|EF-Tu_inhibition|TUFAB|RequiresSNPConfirmation	LN:1185
@SQ	SN:MEG_7329|Drugs|Fosfomycin|Fosfomycin_target_mutation|UHPT|RequiresSNPConfirmation	LN:1380
@SQ	SN:MEG_7330|Drugs|Fosfomycin|Fosfomycin_target_mutation|UHPT|RequiresSNPConfirmation	LN:1392
@SQ	SN:MEG_7333|Drugs|Glycopeptides|VanA-type_resistance_protein|VAN|RequiresSNPConfirmation	LN:1056
@SQ	SN:MEG_7806|Drugs|Lipopeptides|Daptomycin-resistant_mutant|WALK|RequiresSNPConfirmation	LN:1827
@SQ	SN:MEG_7840|Drugs|Lipopeptides|Defensin-resistant_mutant|YKKCL|RequiresSNPConfirmation	LN:2571
@SQ	SN:MEG_7843|Drugs|Lipopeptides|Daptomycin-resistant_mutant|YYBT|RequiresSNPConfirmation	LN:1977
"""

geneDict = {}

FullName = []
FullName.append("MEG_4095|Drugs|Fosfomycin|Fosfomycin_target_mutation|MURA|RequiresSNPConfirmation")
FullName.append("MEG_4130|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|NDH|RequiresSNPConfirmation")
FullName.append("MEG_5328|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation")
FullName.append("MEG_5331|Drugs|Fluoroquinolones|Fluoroquinolone-resistant_DNA_topoisomerases|PARC|RequiresSNPConfirmation")
FullName.append("MEG_5401|Drugs|betalactams|Penicillin_binding_protein|PBP2|RequiresSNPConfirmation")
FullName.append("MEG_411|Multi-compound|Drug_and_biocide_resistance|Drug_and_biocide_RND_efflux_regulator|ACRR|RequiresSNPConfirmation")
FullName.append("MEG_6090|Drugs|Rifampin|Rifampin-resistant_beta-subunit_of_RNA_polymerase_RpoB|RPOB|RequiresSNPConfirmation")


def SNPTest(SNP_Num, fullName, start, end, cigar, SEQ):
    line1 = []
    line2 = []
    line1.append("Test_" + SNP_Num.__str__())
    line2.append(line1[0])
    line1.append("99")
    line2.append("147")
    line1.append(fullName)
    line2.append(line1[2])
    line1.append(start.__str__())
    line2.append(line1[3])
    line1.append("255")
    line2.append(line1[4])
    line1.append(cigar)
    line2.append(cigar)
    line1.append("=")
    line2.append(line1[6])
    line1.append(line1[3])
    line2.append(line1[3])
    line1.append((end-(start-1)).__str__())
    line2.append("-" + line1[8])
    line1.append(SEQ)
    line2.append(SEQ)
    line1.append("*")
    line2.append(line1[10])
    toReturn = ""
    for tab in line1:
        toReturn = toReturn + tab + "\t"
    toReturn = toReturn + "\n"
    for tab in line2:
        toReturn = toReturn + tab + "\t"
    toReturn = toReturn + "\n"
    return toReturn
def makeTest(SNP_Num, fullName, aa_seq, cigar, start, end):
    nt_seq = ""
    for aa in aa_seq:
        nt_seq = nt_seq + reverseTranslation(aa)
    indexStart = (start-1) % 3
    indexEnd = end % 3
    nt_seq = nt_seq[indexStart:]
    if indexEnd != 0:
        indexEnd = 3 - indexEnd
        nt_seq = nt_seq[:-1*indexEnd]
    return SNPTest(SNP_Num, fullName, start, end, cigar, nt_seq)
def sortSnpInfo(snpInfo):
    snpFirst = snpInfo[0:int(len(snpInfo)/2)]
    if len(snpFirst) > 1:
        snpFirst = sortSnpInfo(snpFirst)
    snpLast = snpInfo[int(len(snpInfo)/2):len(snpInfo)]
    if len(snpLast) > 1:
        snpLast = sortSnpInfo(snpLast)
    toReturn = []
    for i in range(0, len(snpInfo)):
        if len(snpFirst) == 0:
            toReturn.append(snpLast.pop(0))
        elif len(snpLast) == 0:
            toReturn.append(snpFirst.pop(0))
        else:
            if (snpFirst[0][1][0] if type(snpFirst[0][1]) == list else snpFirst[0][1]) < (snpLast[0][1][0] if type(snpLast[0][1]) == list else snpLast[0][1]):
                toReturn.append(snpFirst.pop(0))
            else:
                toReturn.append(snpLast.pop(0))
    return toReturn
def nucleicMustTest(mustInfo, gene, SNP_Num):
    start = mustInfo.getPos()-26
    if start < 1: start = 1
    sequence = gene.ntSequence()
    SEQ = sequence[start-1:(mustInfo.getPos()-1)]
    cigar = "20H"
    lastNt = mustInfo.getPos()-1
    while mustInfo != None:
        if lastNt < mustInfo.getPos()-1:
            SEQ = SEQ + sequence[lastNt:mustInfo.getPos()-1]
        SEQ = SEQ + mustInfo.getWt()
        lastNt = mustInfo.getPos()
        end = mustInfo.getPos()+ 25
        mustInfo = mustInfo.getNext()
    if end > gene.ntSeqLength(): end = gene.ntSeqLength()
    cigar = cigar + str(end - (start - 1)) + "M20H"
    SEQ = SEQ + sequence[lastNt:end]
    return SNPTest(SNP_Num, gene.getFullName(), start, end, cigar, SEQ)
def mustTest(mustInfo, gene, SNP_Num):
    if gene.rRna(): return nucleicMustTest(mustInfo, gene, SNP_Num)
    start = mustInfo.getPos()*3-23
    if start < 1: start = 1
    sequence = gene.ntSequence()
    SEQ = sequence[start-1:(mustInfo.getPos()*3-3)]
    cigar = "20H"
    lastNt = mustInfo.getPos()*3-3
    while mustInfo != None:
        if lastNt < mustInfo.getPos()*3-3:
            SEQ = SEQ + sequence[lastNt:mustInfo.getPos()*3-3]
        SEQ = SEQ + reverseTranslation(mustInfo.getWt())
        lastNt = mustInfo.getPos()*3
        end = mustInfo.getPos()*3 + 21
        mustInfo = mustInfo.getNext()
    if end > gene.ntSeqLength(): end = gene.ntSeqLength()
    cigar = cigar + str(end - (start - 1)) + "M20H"
    SEQ = SEQ + sequence[lastNt:end]
    return SNPTest(SNP_Num, gene.getFullName(), start, end, cigar, SEQ)
def multipleSNPTest(snpInfo, gene, SNP_Num):
    if gene.rRna(): return multipleNucleicSNPTest(snpInfo, gene, SNP_Num)
    snpInfo = sortSnpInfo(snpInfo)
    start = (snpInfo[0][1][0] if type(snpInfo[0][1]) == list else snpInfo[0][1])*3-23
    end = (snpInfo[-1][1][0] if type(snpInfo[-1][1]) == list else snpInfo[-1][1])*3+21
    if (start < 1) : start = 1
    if end > gene.ntSeqLength(): end = gene.ntSeqLength()
    inBetweenH = []
    lastNt = start - 1
    lastIsM = False
    lastIsI = False
    lastIsD = False
    for snp in snpInfo:
        if (lastNt < (snp[1][0] if type(snp[1]) == list else snp[1])*3 - 3):
            if not(lastIsM): #wt435-, wt437-/mt
                inBetweenH.append(((((snp[1][0] if type(snp[1]) == list else snp[1])*3-3) - lastNt),'M'))
                lastIsM = True
                lastIsI = False
                lastIsD = False
            else: #wt435mt, wt437-/mt
                inBetweenH[-1] = (inBetweenH[-1][0] + (((snp[1][0] if type(snp[1]) == list else snp[1])*3-3) - lastNt), 'M')
        if snp[2][0] == "-":
            if not(lastIsD): #wt436mt, wt437-; wt435-/mt, wt437-
                lastIsD = True
                lastIsI = False
                lastIsM = False
                inBetweenH.append((3, 'D'))
            else: #wt436-,wt437-
                inBetweenH[-1] = (inBetweenH[-1][0] + 3, 'D')
        elif snp[2][0] == "+":
            if not(lastIsI): #wt436mt, wt437-; wt435-/mt, wt437-
                lastIsM = False
                lastIsD = False
                lastIsI = True
                inBetweenH.append((3 * len(snp[0]), 'I'))
            else:
                inBetweenH[-1] = (inBetweenH[-1][0] + 3 * len(snp[0]), 'I')

        else:
            if (lastIsM): #wt436mt, wt437mt; #wt435-/mt, wt437mt:
                inBetweenH[-1] = (inBetweenH[-1][0] + 3, 'M')
            else: #wt436-,wt437mt
                lastIsM = True
                lastIsD = False
                lastIsI = False
                inBetweenH.append((3, 'M'))
        if (snp[2]) == "-":
            lastNt = snp[1][0]*3
        elif (snp[2]) != "+":
            lastNt = snp[1]*3
    if lastIsM:
        inBetweenH[-1] = (inBetweenH[-1][0] + end - (snpInfo[-1][1][0] if type(snpInfo[-1][1]) == list else snpInfo[-1][1])*3, 'M')
    elif end > (snpInfo[-1][1][0] if type(snpInfo[-1][1]) == list else snpInfo[-1][1])*3:
        inBetweenH.append((end - lastNt, 'M'))
    cigar = "20H"
    for next in inBetweenH:
        cigar = cigar + str(next[0]) + next[1]
    cigar = cigar + "20H"
    sequence = gene.ntSequence()
    SEQ = sequence[start-1:((snpInfo[0][1][0] if type(snpInfo[0][1]) == list else snpInfo[0][1])*3-3)]
    for i in range(0, len(snpInfo)):
        if snpInfo[i][2][-1] != '-':
            if snpInfo[i][2][-1] == '+':
                for aa in snpInfo[i][0]:
                    SEQ = SEQ + reverseTranslation(aa)
            else:
                SEQ = SEQ + reverseTranslation(snpInfo[i][2][-1])
        if i < (len(snpInfo) - 1):
            SEQ = SEQ + sequence[(snpInfo[i][1][0] if type(snpInfo[i][1]) == list else snpInfo[i][1])*3:(snpInfo[i+1][1][0] if type(snpInfo[i+1][1]) == list else snpInfo[i+1][1])*3-3]
        else:
            SEQ = SEQ + sequence[lastNt:end]
    return SNPTest(SNP_Num, gene.getFullName(), start, end, cigar, SEQ)
def multipleNucleicSNPTest(snpInfo, gene, SNP_Num):
    snpInfo = sortSnpInfo(snpInfo)
    start = snpInfo[0][1]-26
    end = snpInfo[-1][1]+25
    if (start < 1) : start = 1
    if end > gene.ntSeqLength(): end = gene.ntSeqLength()
    inBetweenH = []
    lastNt = start - 1
    lastIsM = False
    for snp in snpInfo:
        if (lastNt < (snp[1][0] if type(snp[1]) == list else snp[1])-1):
            if not(lastIsM): #wt435-, wt437-/mt
                inBetweenH.append((((snp[1][0] if type(snp[1]) == list else snp[1])-1 - lastNt),'M'))
                lastIsM = True
            else: #wt435mt, wt437-/mt
                inBetweenH[-1] = (inBetweenH[-1][0] + ((snp[1][0] if type(snp[1]) == list else snp[1])-1 - lastNt), 'M')
        if snp[2][0] == "-":
            if (lastIsM): #wt436mt, wt437-; wt435-/mt, wt437-
                lastIsM = False
                inBetweenH.append((1, 'D'))
            else: #wt436-,wt437-
                inBetweenH[-1] = (inBetweenH[-1][0] + 1, 'D')
        else:
            if (lastIsM): #wt436mt, wt437mt; #wt435-/mt, wt437mt:
                inBetweenH[-1] = (inBetweenH[-1][0] + 1, 'M')
            else: #wt436-,wt437mt
                lastIsM = True
                inBetweenH.append((1, 'M'))
        if (type(snp[1]) == list):
            lastNt = snp[1][0]
        else:
            lastNt = snp[1]
    if lastIsM:
        inBetweenH[-1] = (inBetweenH[-1][0] + end - (snpInfo[-1][1][0] if type(snpInfo[-1][1]) == list else snpInfo[-1][1]), 'M')
    elif end > (snpInfo[-1][1][0] if type(snpInfo[-1][1]) == list else snpInfo[-1][1]):
        inBetweenH.append((end - (snpInfo[-1][1][0] if type(snpInfo[-1][1]) == list else snpInfo[-1][1]), 'M'))
    cigar = "20H"
    for next in inBetweenH:
        cigar = cigar + str(next[0]) + next[1]
    cigar = cigar + "20H"
    sequence = gene.ntSequence()
    SEQ = sequence[start-1:((snpInfo[0][1][0] if type(snpInfo[0][1]) == list else snpInfo[0][1])-1)]
    for i in range(0, len(snpInfo)):
        if snpInfo[i][2][-1] != '-':
            SEQ = SEQ + snpInfo[i][2][-1]
        if i < (len(snpInfo) - 1):
            SEQ = SEQ + sequence[(snpInfo[i][1][0] if type(snpInfo[i][1]) == list else snpInfo[i][1]):(snpInfo[i+1][1][0] if type(snpInfo[i+1][1]) == list else snpInfo[i+1][1])-1]
        else:
            SEQ = SEQ + sequence[(snpInfo[i][1][0] if type(snpInfo[i][1]) == list else snpInfo[i][1]):end]
    return SNPTest(SNP_Num, gene.getFullName(), start, end, cigar, SEQ)
def deletionTest(snpInfo, gene, SNP_Num):
    toReturn = ""
    for i in snpInfo[1]:
        start = i*3-23
        end = i*3+21
        if (start < 1) : start = 1
        if end > gene.ntSeqLength(): end = gene.ntSeqLength()
        cigar = "20H"
        if i != 1:
            cigar = cigar + str((i*3-3)-(start-1))+ "M3D"
        if i != gene.ntSeqLength():
            cigar = cigar + str(end-i*3) + "M20H"
        sequence = gene.ntSequence()
        SEQ = sequence[start-1:(i*3-3)] + sequence[(i*3):end]
        toReturn = toReturn + SNPTest(str(SNP_Num) +"a"+str(i), gene.getFullName(), start, end, cigar, SEQ)
        cigar = "20H"
        if i != 1:
            cigar = cigar + str((i*3-4)-(start-1)) + "M3D"
        if i != gene.ntSeqLength():
            cigar = cigar + str(end-(i*3)+1) + "M20H"
        sequence = gene.ntSequence()
        SEQ = sequence[start-1:(i*3-4)] + sequence[(i*3)-1:end]
        toReturn = toReturn + SNPTest(str(SNP_Num) +"b"+str(i), gene.getFullName(), start, end, cigar, SEQ)
        cigar = "20H"
        if i != 1:
            cigar = cigar + str((i*3-2)-(start-1)) + "M3D"
        if i != gene.ntSeqLength():
            cigar = cigar + str(end-(i*3)-1) + "M20H"
        sequence = gene.ntSequence()
        SEQ = sequence[start-1:(i*3-2)] + sequence[(i*3)+1:end]
        toReturn = toReturn + SNPTest(str(SNP_Num) +"c"+str(i), gene.getFullName(), start, end, cigar, SEQ)
    return toReturn
def insertionTest(snpInfo, gene, SNP_Num):
    toReturn = ""
    for i in snpInfo[1]:
        start = i*3-23
        end = i*3+21
        if (start < 1) : start = 1
        if end > gene.ntSeqLength(): end = gene.ntSeqLength()
        cigar = "20H"
        if i != 1:
            cigar = cigar + str((i*3-3)-(start-1))+ "M" + str(3 * len(snpInfo[0])) + "I"
        if i != gene.ntSeqLength():
            cigar = cigar + str(end-i*3+3) + "M20H"
        sequence = gene.ntSequence()
        inserted = ""
        for aa in snpInfo[0]:
            inserted = inserted + reverseTranslation(aa)
        SEQ = sequence[start-1:(i*3-3)] + inserted + sequence[(i*3)-3:end]
        toReturn = toReturn + SNPTest(str(SNP_Num) +"a"+str(i), gene.getFullName(), start, end, cigar, SEQ)
    if (len(snpInfo[1]) > 1) and (len(snpInfo[0]) > 1):
        start = snpInfo[1][0]*3-20
        end = snpInfo[1][0]*3+24
        if (start < 1) : start = 1
        if end > gene.ntSeqLength(): end = gene.ntSeqLength()
        cigar = "20H"
        if snpInfo[1][0] != 1:
            cigar = cigar + str((snpInfo[1][0]*3)-(start-1))+ "M" + str(3 * len(snpInfo[0])) + "I"
        if snpInfo[1][0] != gene.ntSeqLength():
            cigar = cigar + str(end-snpInfo[1][0]*3) + "M20H"
        sequence = gene.ntSequence()
        inserted = ""
        for aa in snpInfo[0][1:]:
            inserted = inserted + reverseTranslation(aa)
        inserted = inserted + reverseTranslation(snpInfo[0][0])
        SEQ = sequence[start-1:(snpInfo[1][0]*3)] + inserted + sequence[(snpInfo[1][0]*3):end]
        toReturn = toReturn + SNPTest(str(SNP_Num) +"a"+str(snpInfo[1]), gene.getFullName(), start, end, cigar, SEQ)
    return toReturn
def singleSNPTest(snpInfo, gene, SNP_Num):
    if gene.rRna(): return singleNucleicSNPTest(snpInfo, gene, SNP_Num)
    if snpInfo[2] == "-": return deletionTest(snpInfo, gene, SNP_Num)
    elif snpInfo[2] == "+": return insertionTest(snpInfo, gene, SNP_Num)
    start = snpInfo[1]*3-23
    end = snpInfo[1]*3+21
    if (start < 1) : start = 1
    if end > gene.ntSeqLength(): end = gene.ntSeqLength()
    cigar = "20H" + (end - (start -1)).__str__() + "M20H"
    if snpInfo[2][0] == "-":
        cigar = "20H"
        if snpInfo[1] != 1:
            cigar = cigar + ((snpInfo[1]*3-3)-(start-1)).__str__() + "M3D"
        if snpInfo[1] != gene.ntSeqLength():
            cigar = cigar + (end-snpInfo[1]*3).__str__() + "M20H"
    sequence = gene.ntSequence()
    SEQ = sequence[start-1:(snpInfo[1]*3-3)] + reverseTranslation(snpInfo[2][-1]) + sequence[(snpInfo[1]*3):end]
    return SNPTest(SNP_Num, gene.getFullName(), start, end, cigar, SEQ)
def singleNucleicSNPTest(snpInfo, gene, SNP_Num):
    snpPos = (snpInfo[1][0] if type(snpInfo[1]) == list else snpInfo[1])
    start = snpPos - 26
    end = snpPos + 25
    if start < 1: start = 1
    if end > gene.ntSeqLength(): end = gene.ntSeqLength()
    cigar = "20H" + (end - (start -1)).__str__() + "M20H"
    if snpInfo[2][0] == "-":
        cigar = "20H"
        if snpPos != 1:
            cigar = cigar + ((snpPos)-(start-1)).__str__() + "M1D"
        if snpPos != gene.ntSeqLength():
            cigar = cigar + (end-snpPos).__str__() + "M20H"
    sequence = gene.ntSequence()
    SEQ = sequence[start-1:(snpPos-1)] + snpInfo[2][-1] + sequence[(snpPos):end]
    return SNPTest(SNP_Num, gene.getFullName(), start, end, cigar, SEQ)

SNPinfo = open("extracted_SNP_files/SNPinfo.fasta", "rt")
isSequence = False
name = ""
snp = ""
sequence = ""
for line in SNPinfo:
    if isSequence:
        sequence = line
        geneDict.update({name + "|RequiresSNPConfirmation":Gene(name, sequence[:-1], snp)})
        isSequence = False
    else:
        temp = 0
        for i in range(0, 5):
            temp = line[temp+1:].find('|') + temp + 1
        name = line[1:temp]
        snp = line[temp+1:len(line)-1]
        isSequence = True
SNPinfo.close()

def Test1():
    SAM_file = open("Test/Test.sam", "w")
    SNP_Num = 1
    SAM_file.write(header)
    for gene in geneDict.values():
        for snp in gene.condensedMisInDelInfo():
            SAM_file.write(singleSNPTest(snp, gene, SNP_Num))
            SNP_Num+=1
        for snp in gene.condensedNonInfo():
            SAM_file.write(singleSNPTest(snp, gene, SNP_Num))
            SNP_Num+=1
        for snp in gene.condensedMultInfo():
            SAM_file.write(multipleSNPTest(snp[0], gene, SNP_Num))
            SNP_Num+=1
        must = gene.getFirstMustBetweenParams(1, gene.ntSeqLength())
        if must == None:
            continue
        SAM_file.write(mustTest(must[0], gene, SNP_Num))
        SNP_Num+=1
        if must[0].getNext() != None:
            SAM_file.write(mustTest(must[0].getNext(), gene, SNP_Num))
            SNP_Num+=1
    SAM_file.close()
def Test2():
    SAM_file = open("Test/Test2.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(multipleSNPTest([('Y', 147, ('*',)), ('G', 146, ('*',))], geneDict.get("MEG_2866|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethionamide-resistant_mutant|ETHA|RequiresSNPConfirmation"), SNP_Num))
    SNP_Num+=1
    SAM_file.write(multipleSNPTest([('Y', 147, ('*',)), ('S', 149, ('*',))], geneDict.get("MEG_2866|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethionamide-resistant_mutant|ETHA|RequiresSNPConfirmation"), SNP_Num))
    SNP_Num+=1
    SAM_file.write(multipleSNPTest([('Y', 147, ('*',)), ('C', 131, ('*',))], geneDict.get("MEG_2866|Drugs|Mycobacterium_tuberculosis-specific_Drug|Ethionamide-resistant_mutant|ETHA|RequiresSNPConfirmation"), SNP_Num))
    SNP_Num+=1
    SAM_file.write(multipleSNPTest([('W', 98, ('*',)), ('R', 99, ('*',))], geneDict.get("MEG_7250|Drugs|Mycobacterium_tuberculosis-specific_Drug|Para-aminosalicylic_acid_resistant_mutant|THYA|RequiresSNPConfirmation"), SNP_Num))
    SNP_Num+=1
    SAM_file.write(multipleSNPTest([('W', 98, ('*',)), ('S', 105, ('*',))], geneDict.get("MEG_7250|Drugs|Mycobacterium_tuberculosis-specific_Drug|Para-aminosalicylic_acid_resistant_mutant|THYA|RequiresSNPConfirmation"), SNP_Num))
    SNP_Num+=1
    SAM_file.write(multipleSNPTest([('W', 98, ('*',)), ('V', 96, ('*',))], geneDict.get("MEG_7250|Drugs|Mycobacterium_tuberculosis-specific_Drug|Para-aminosalicylic_acid_resistant_mutant|THYA|RequiresSNPConfirmation"), SNP_Num))
    SNP_Num+=1
    SAM_file.write(multipleSNPTest([('G', 84, ('D',)), ('L', 100, ('P',)), ('A', 115, ('T',)), ('Y', 122, ('N',))], geneDict.get("MEG_4132|Drugs|Mycobacterium_tuberculosis-specific_Drug|Isoniazid-resistant_mutant|NDH|RequiresSNPConfirmation"), SNP_Num))
    SNP_Num+=1
    SAM_file.write(multipleSNPTest([('Q', 10, ('*',)), ('D', 12, ('A',)), ('L', 19, ('P',)), ('C', 14, ('Y',)), ('G', 23, ('V',))], geneDict.get("MEG_5803|Drugs|Mycobacterium_tuberculosis-specific_Drug|Pyrazinamide-resistant_mutant|PNCA|RequiresSNPConfirmation"), SNP_Num))
    SAM_file.close()
def InsertionTest1():
    SAM_file = open("Test/Insertion1.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[0], "TNLR", "20H1M3I8M20H", 369 * 3 - 2, 371 * 3)) #Test with mt second
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[1], "CFRH", "20H1M3I8M20H", 13 * 3 - 2, 15 * 3)) #Test with mt first
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[2], "WWSI", "20H1M3I8M20H", 83 * 3 - 2, 85 * 3)) #Test with mt in both
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[3], "VINN", "20H1M3I8M20H", 103 * 3 - 2, 105 * 3)) #Test with wt first, mt second
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[4], "VARK", "20H1M3I8M20H", 501 * 3 - 2, 503 * 3)) #Test with mt first, wt second
    SAM_file.close()
def InsertionTest2():
    SAM_file = open("Test/Insertion2_1.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "TTCGA", "20H3M3I9M20H", 44 * 3 - 2, 47 * 3)) #Test with mt after insertion
    SAM_file.close()

    SAM_file = open("Test/Insertion2_2.sam", "w")
    SAM_file.write(header)
    SAM_file.write(makeTest(SNP_Num, FullName[5], "TRCGA", "20H3M3I9M20H", 44 * 3 - 2, 47 * 3)) #Test with wt in insertion, mt after insertion
    SAM_file.close()

    SAM_file = open("Test/Insertion2_3.sam", "w")
    SAM_file.write(header)
    SAM_file.write(makeTest(SNP_Num, FullName[5], "TCRGA", "20H3M3I9M20H", 44 * 3 - 2, 47 * 3)) #Test with mt in insertion, wt after insertion
    SAM_file.close()
def InsertionTest3():
    SAM_file = open("Test/Insertion3.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[0], "ATNLR", "20H3M1I3M2I6M20H", 368 * 3 - 2, 371 * 3)) #Test with mt second
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[1], "PCFRH", "20H3M1I3M2I6M20H", 12 * 3 - 2, 15 * 3)) #Test with mt first
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[2], "DWWSI", "20H3M1I3M2I6M20H", 82 * 3 - 2, 85 * 3)) #Test with mt in both
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[3], "TVINN", "20H3M1I3M2I6M20H", 102 * 3 - 2, 105 * 3)) #Test with wt first, mt second
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[4], "TVARK", "20H3M1I3M2I6M20H", 500 * 3 - 2, 503 * 3)) #Test with mt first, wt second
    SAM_file.close()
def InsertionTest4():
    SAM_file = open("Test/Insertion4_1.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[0], "MATNL", "20H3M1I6M2I3M20H", 367 * 3 - 2, 370 * 3)) #Test with mt second; second insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[1], "PPCFR", "20H3M1I6M2I3M20H", 11 * 3 - 2, 14 * 3)) #Test with mt first; second insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[2], "GDWWS", "20H3M1I6M2I3M20H", 81 * 3 - 2, 84 * 3)) #Test with mt in both; second insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[3], "RTVIN", "20H3M1I6M2I3M20H", 101 * 3 - 2, 104 * 3)) #Test with wt first, mt second; second insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[4], "GTVAR", "20H3M1I6M2I3M20H", 499 * 3 - 2, 502 * 3)) #Test with mt first, wt second; second insertion chunk
    SAM_file.close()

    SAM_file = open("Test/Insertion4_2.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[0], "ATNLR", "20H3M1I6M2I3M20H", 368 * 3 - 2, 371 * 3)) #Test with mt second; first insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[1], "PCFRH", "20H3M1I6M2I3M20H", 12 * 3 - 2, 15 * 3)) #Test with mt first; first insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[2], "DWWSI", "20H3M1I6M2I3M20H", 82 * 3 - 2, 85 * 3)) #Test with mt in both; first insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[3], "TVINN", "20H3M1I6M2I3M20H", 102 * 3 - 2, 105 * 3)) #Test with wt first, mt second; first insertion chunk
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[4], "TVARK", "20H3M1I6M2I3M20H", 500 * 3 - 2, 503 * 3)) #Test with mt first, wt second; first insertion chunk
    SAM_file.close()
def InsertionTest5():
    SAM_file = open("Test/Insertion5.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "RCGA", "20H1M3I7M20H", 45 * 3 - 1, 47 * 3)) #Test with mt in insertion
    SAM_file.close()
def DeletionTest1():
    SAM_file = open("Test/Deletion1.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[6], "HQN", "20H1M9D8M20H", 432 * 3 - 2, 437 * 3)) #Test with deletion mutations
    SNP_Num  += 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "CGA", "20H1M3D8M20H", 44 * 3 - 2, 47 * 3)) #Test with deletion making mt
    SAM_file.close()
def DeletionTest2():
    SAM_file = open("Test/Deletion2.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "GVTC", "20H1M2D8M1D2M20H", 41 * 3 - 1, 45 * 3)) #Test with mt at last deletion chunk
    SAM_file.close()
def InsertionTest6():
    SAM_file = open("Test/Insertion6.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "GVTCG", "20H1M1I6M2I4M20H", 43 * 3 - 1, 46 * 3)) #Test with mt last insertion chunk
    SAM_file.close()
def DeletionTest3():
    SAM_file = open("Test/Deletion3_1.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "CGAI", "20H1M1D8M2D3M20H", 45 * 3 - 2, 49 * 3)) #Test with mt at first deletion chunk
    SAM_file.close()

    SAM_file = open("Test/Deletion3_2.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "GVTC", "20H1M1D8M2D3M20H", 41 * 3 - 2, 45 * 3)) #Test with mt at last deletion chunk
    SAM_file.close()
def InsertionDeletionTest1():
    SAM_file = open("Test/InsertionDeletion1_1.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "TCGAI", "20H3M1D9M1I2M20H", 44 * 3 - 2, 48 * 3)) #Test with mt at deletion chunk
    SAM_file.close()

    SAM_file = open("Test/InsertionDeletion1_2.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "AGVTC", "20H3M1D9M1I2M20H", 41 * 3 - 2, 45 * 3)) #Test with mt at insertion chunk
    SAM_file.close()
def InsertionDeletionTest2():
    SAM_file = open("Test/InsertionDeletion2_1.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "CGAI", "20H1M1I8M1D2M20H", 45 * 3 - 2, 48 * 3)) #Test with mt at insertion chunk
    SAM_file.close()

    SAM_file = open("Test/InsertionDeletion2_2.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "GVTC", "20H1M1I8M1D2M20H", 42 * 3 - 2, 45 * 3)) #Test with mt at deletion chunk
    SAM_file.close()
def InsertionDeletionTest3():
    SAM_file = open("Test/InsertionDeletion3.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "C", "20H1D1M1I1M20H", 45 * 3 - 2, 45 * 3)) 
    SAM_file.close()
def InsertionDeletionTest4():
    SAM_file = open("Test/InsertionDeletion4.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[5], "C", "20H1I1M1D1M20H", 45 * 3 - 2, 45 * 3)) 
    SAM_file.close()
def DeletionTest4():
    SAM_file = open("Test/Deletion4.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[6], "FNP", "20H1M12D6M20H", 433 * 3, 439 * 3)) #Test with deletion mutations
    SAM_file.close()
def DeletionTest5():
    SAM_file = open("Test/Deletion5.sam", "w")
    SAM_file.write(header)
    SNP_Num = 1
    SAM_file.write(makeTest(SNP_Num, FullName[6], "FN", "20H3M12D1M20H", 433 * 3 - 2, 438 * 3 - 2)) #Test with deletion mutations
    SAM_file.close()

Test2()
InsertionTest1()
InsertionTest2()
InsertionTest3()
InsertionTest4()
InsertionTest5()
InsertionTest6()
DeletionTest1()
DeletionTest2()
DeletionTest3()
DeletionTest4()
DeletionTest5()
InsertionDeletionTest1()
InsertionDeletionTest2()
InsertionDeletionTest3()
InsertionDeletionTest4()