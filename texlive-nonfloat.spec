# revision 17598
# category Package
# catalog-ctan /macros/latex/contrib/nonfloat
# catalog-date 2007-01-12 00:17:35 +0100
# catalog-license pd
# catalog-version 1.0
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
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
