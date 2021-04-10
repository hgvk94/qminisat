#include "minisat/utils/System.h"
#include "minisat/utils/ParseUtils.h"
#include "minisat/utils/Options.h"
#include "minisat/core/Dimacs.h"
#include "minisat/core/Solver.h"

using namespace Minisat;

//=================================================================================================


static Solver* solver;
int main(int argc, char** argv) {
    Solver S;
    solver = &S;
    // Use signal handlers that forcibly quit until the solver will be able to respond to
    // interrupts:
    if (argc == 1)
            printf("Reading from standard input... Use '--help' for help.\n");
    gzFile in = (argc == 1) ? gzdopen(0, "rb") : gzopen(argv[1], "rb");
    if (in == NULL)
        printf("ERROR! Could not open file: %s\n", argc == 1 ? "<stdin>" : argv[1]), exit(1);

    if (S.verbosity > 0) {
            printf("============================[ Problem Statistics ]=============================\n");
            printf("|                                                                             |\n");
    }

    parse_DIMACS(in, S, true);
    gzclose(in);
    FILE* res = (argc >= 3) ? fopen(argv[2], "wb") : NULL;

    if (S.verbosity > 0){
        printf("|  Number of variables:  %12d                                         |\n", S.nVars());
        printf("|  Number of clauses:    %12d                                         |\n", S.nClauses()); }
    S.print_circuit();
}
