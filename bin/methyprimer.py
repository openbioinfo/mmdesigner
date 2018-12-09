import glob
import os
import sys
scr_dir = os.path.dirname(os.path.realpath(__file__))
mod_dir = os.path.join(scr_dir,"../")
sys.path.insert(0,mod_dir)

from methyprimer.get_target_region.get_target_region import get_target_region
from methyprimer.primer3_design.primer3_design import primer3_design
from methyprimer.filter_primer.CpG_filter import CpG_filter
from methyprimer.bisuffle_fasta.bisuffle_fasta import bisuffle_fasta
from methyprimer.proper_primer.properPrimers import properPrimers
from methyprimer.combine_primer.greedySearch import greedySearch
from methyprimer.combine_primer.formatOut import formatOut
from methyprimer.verify_primer.verify_primer import verify_primer


def main(bed,ref,prefix):
    
    target_fa = get_target_region(bed,ref,prefix)
    p3outfile = primer3_design(target_fa,prefix)
    filter_primer = CpG_filter(p3outfile,prefix)
    final_pre_primer = bisuffle_fasta(filter_primer,prefix)	
    pid2pids,sid2pids = properPrimers(final_pre_primer,prefix)
    greedySearch(sid2pids,pid2pids,prefix)
    out = formatOut(prefix)
    verify_primer(final_pre_primer,out,prefix)    


if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        test.py [options] -i <bed> -r <ref_genome> -p <prefix>

    Options:
        -i,--input=input_bed
        -r,--ref=ref_genome
        -p,--prefix=prefix

    """
    args = docopt(usage)
    print args
    bed = args["--input"]
    ref = args["--ref"]
    prefix = args["--prefix"]
    main(bed,ref,prefix)
