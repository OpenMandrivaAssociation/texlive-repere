# revision 32455
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-repere
Version:	20140214
Release:	4
Summary:	TeXLive repere package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repere.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/repere.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive repere package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/repere/repere.mp
%doc %{_texmfdistdir}/doc/metapost/repere/README
%doc %{_texmfdistdir}/doc/metapost/repere/repere-doc.pdf
%doc %{_texmfdistdir}/doc/metapost/repere/repere-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
