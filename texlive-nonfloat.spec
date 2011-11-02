Name:		texlive-nonfloat
Version:	1.0
Release:	1
Summary:	Non-floating table and figure captions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nonfloat
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nonfloat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Adjusts the figure and table environments to ensure that
centered objects as one line captions are centered as well.
Also the vertical spaces for table captions above the table are
changed.

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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
