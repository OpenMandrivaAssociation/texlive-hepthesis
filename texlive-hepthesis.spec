# revision 18725
# category Package
# catalog-ctan /macros/latex/contrib/hepthesis
# catalog-date 2010-06-03 14:28:33 +0200
# catalog-license lppl
# catalog-version 1.4.3
Name:		texlive-hepthesis
Version:	1.4.3
Release:	1
Summary:	A class for academic reports, especially PhD theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hepthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Hepthesis is a LaTeX class for typesetting large academic
reports, in particular PhD theses. It was originally developed
for typesetting the author's high-energy physics PhD thesis and
includes some features specifically tailored to such an
application. In particular, hepthesis offers: - Attractive
semantic environments for various rubric sections; - Extensive
options for draft production, screen viewing and binding-ready
output; - Helpful extensions of existing environments,
including equation and tabular; and - Support for quotations at
the start of the thesis and each chapter. The class is based on
scrbook, from the KOMA-Script bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hepthesis/hepthesis.cls
%doc %{_texmfdistdir}/doc/latex/hepthesis/ChangeLog
%doc %{_texmfdistdir}/doc/latex/hepthesis/Makefile
%doc %{_texmfdistdir}/doc/latex/hepthesis/README
%doc %{_texmfdistdir}/doc/latex/hepthesis/TODO
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/Makefile
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/appendices.tex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/backmatter.tex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/chap1.tex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/chap2.tex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/chap3.tex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/ckmfitter-alpha-combined.pdf
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/example.pdf
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/example.tex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/extrastyles.zip
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/frontmatter.tex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/getNewBibtex
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/h-physrev.bst
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/lhcb-detector-cross-section.pdf
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/mythesis.bib
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/mythesis.cls
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/mythesis.sty
%doc %{_texmfdistdir}/doc/latex/hepthesis/example/mythesismath.sty
%doc %{_texmfdistdir}/doc/latex/hepthesis/hepthesis.pdf
%doc %{_texmfdistdir}/doc/latex/hepthesis/hepthesis.tex
#- source
%doc %{_texmfdistdir}/source/latex/hepthesis/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}