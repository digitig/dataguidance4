If compiling on a local PC:

mkdir obj

pdflatex -output-directory obj main

bibtex obj/main
makeindex obj/main
makeindex obj/locationidx

% Work-around because printindex doesn't look in the output-directory:
ln -s obj/main.idx
ln -s obj/locationidx.idx

pdflatex -output-directory obj main
pdflatex -output-directory obj main
pdflatex -output-directory obj main

% is-unsrt.bst is Nelson Beebe's bibtex extensions, to include ISBN and
% other features.
