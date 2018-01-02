Name:		texlive-hepthesis
Version:	1.5.2
Release:	1
Summary:	A class for academic reports, especially PhD theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hepthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepthesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hepthesis
%doc %{_texmfdistdir}/doc/latex/hepthesis

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
