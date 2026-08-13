%global tl_name omega
%global tl_revision 33046

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A wide-character-set extension of TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/systems/omega
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/omega.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/omega.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
A development of TeX, which deals in multi-octet Unicode characters, to
enable native treatment of a wide range of languages without changing
character-set. Work on Omega has ceased (the TeX Live package contains
only support files); its compatible successor is aleph, which is itself
also in major maintenance mode only. Ongoing projects developing Omega
(and Aleph) ideas include Omega-2 and LuaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from omega:
Map omega.map
TL_DROPIN_EOF
