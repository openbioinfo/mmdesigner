import os


def main(locs,ref):

    pass




if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        methyprimer.py [options] -i <input> -r <ref>

    Options:
        -i,--input=locs_file  e.g.: chr7:55242466
        -r,--ref=methy_reference_genome_dir

    Description:
        methyprimer is used for design human methylation multiplex PCR primer.

    """
    args = docopt(usage)
    print args
    locs = args["--input"]
    ref = args["--ref"]
    main(locs,ref)
