%global tl_name nonfloat
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Non-floating table and figure captions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nonfloat
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Adjusts the figure and table environments to ensure that centered
objects as one line captions are centered as well. Also the vertical
spaces for table captions above the table are changed.

