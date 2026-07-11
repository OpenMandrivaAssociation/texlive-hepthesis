%global tl_name hepthesis
%global tl_revision 46054

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.2
Release:	%{tl_revision}.1
Summary:	A class for academic reports, especially PhD theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hepthesis
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hepthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hepthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hepthesis is a LaTeX class for typesetting large academic reports, in
particular PhD theses. It was originally developed for typesetting the
author's high-energy physics PhD thesis and includes some features
specifically tailored to such an application. In particular, hepthesis
offers: Attractive semantic environments for various rubric sections;
Extensive options for draft production, screen viewing and binding-ready
output; Helpful extensions of existing environments, including equation
and tabular; and Support for quotations at the start of the thesis and
each chapter. The class is based on scrbook, from the KOMA-Script
bundle.

