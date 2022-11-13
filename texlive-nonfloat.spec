Name:		texlive-nonfloat
Version:	17598
Release:	1
Summary:	Non-floating table and figure captions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nonfloat
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Adjusts the figure and table environments to ensure that
centered objects as one line captions are centered as well.
Also the vertical spaces for table captions above the table are
changed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nonfloat/nonfloat.sty
%doc %{_texmfdistdir}/doc/latex/nonfloat/nonfloat-en.pdf
%doc %{_texmfdistdir}/doc/latex/nonfloat/nonfloat-en.tex
%doc %{_texmfdistdir}/doc/latex/nonfloat/nonfloat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nonfloat/nonfloat.drv
%doc %{_texmfdistdir}/source/latex/nonfloat/nonfloat.dtx
%doc %{_texmfdistdir}/source/latex/nonfloat/nonfloat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
