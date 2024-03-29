Name:		texlive-omega
Version:	33046
Release:	2
Summary:	A wide-character-set extension of TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/omega
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/omega.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/omega.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A development of TeX, which deals in multi-octet Unicode
characters, to enable native treatment of a wide range of
languages without changing character-set. Work on Omega seems,
more or less, to have ceased: its immediate successor was to be
the aleph project (though that too has stalled). Projects
developing Omega (and Aleph) ideas include Omega-2 and LuaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/omega/config.omega
%{_texmfdistdir}/dvips/omega/omega.cfg
%{_texmfdistdir}/fonts/afm/public/omega/omsea1.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsea1b.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsea2.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsea2b.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsea3.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsea3b.afm
%{_texmfdistdir}/fonts/afm/public/omega/omseco.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsecob.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsecobi.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsecoi.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsecx.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsecy.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsegr.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsegrb.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsegrbi.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsegri.afm
%{_texmfdistdir}/fonts/afm/public/omega/omseha.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsehe.afm
%{_texmfdistdir}/fonts/afm/public/omega/omseip.afm
%{_texmfdistdir}/fonts/afm/public/omega/omsela.afm
%{_texmfdistdir}/fonts/afm/public/omega/omselab.afm
%{_texmfdistdir}/fonts/afm/public/omega/omselabi.afm
%{_texmfdistdir}/fonts/afm/public/omega/omselai.afm
%{_texmfdistdir}/fonts/afm/public/omega/omseti.afm
%{_texmfdistdir}/fonts/map/dvips/omega/omega.map
%{_texmfdistdir}/fonts/ofm/public/omega/omarab.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/omarabb.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/omlgc.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/omlgcb.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/omlgcbi.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/omlgci.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/ucitt10.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/ucsltt10.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/uctt10.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/uctt12.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/uctt8.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/uctt9.ofm
%{_texmfdistdir}/fonts/ofm/public/omega/ucvtt10.ofm
%{_texmfdistdir}/fonts/ovf/public/omega/omarab.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/omarabb.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/omlgc.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/omlgcb.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/omlgcbi.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/omlgci.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/ucitt10.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/ucsltt10.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/uctt10.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/uctt12.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/uctt8.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/uctt9.ovf
%{_texmfdistdir}/fonts/ovf/public/omega/ucvtt10.ovf
%{_texmfdistdir}/fonts/ovp/public/omega/omarab.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/omarabb.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/omlgc.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/omlgcb.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/omlgcbi.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/omlgci.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/ucitt10.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/ucsltt10.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/uctt10.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/uctt12.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/uctt8.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/uctt9.ovp
%{_texmfdistdir}/fonts/ovp/public/omega/ucvtt10.ovp
%{_texmfdistdir}/fonts/tfm/public/omega/omding.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsea1.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsea1b.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsea2.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsea2b.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsea3.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsea3b.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omseco.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsecob.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsecobi.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsecoi.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsecx.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsecy.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsegr.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsegrb.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsegrbi.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsegri.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omseha.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omseip.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omsela.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omselab.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omselabi.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omselai.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omseti.tfm
%{_texmfdistdir}/fonts/tfm/public/omega/omssti.tfm
%{_texmfdistdir}/fonts/type1/public/omega/omding.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsea1.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsea1b.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsea2.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsea2b.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsea3.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsea3b.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omseco.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsecob.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsecobi.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsecoi.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsecx.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsecy.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsecyb.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsecyi.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsegr.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsegrb.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsegrbi.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsegri.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omseha.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsehe.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omseip.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omsela.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omselab.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omselabi.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omselai.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omseti.pfb
%{_texmfdistdir}/fonts/type1/public/omega/omssti.pfb
%{_texmfdistdir}/omega/ocp/char2uni/in646.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88591.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88592.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88593.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88594.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88595.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88596.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88597.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88598.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in88599.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in8859a.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in8859d.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in8859e.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in8859f.ocp
%{_texmfdistdir}/omega/ocp/char2uni/in8859g.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inatari.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inav.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inbig5.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1250.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1251.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1252.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1253.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1254.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1255.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1256.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1257.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp1258.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp866.ocp
%{_texmfdistdir}/omega/ocp/char2uni/incp874.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inebcdic.ocp
%{_texmfdistdir}/omega/ocp/char2uni/ingb.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inkoi8.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inmac.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inmsdos.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inmsdos2.ocp
%{_texmfdistdir}/omega/ocp/char2uni/innext.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inov.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inps2.ocp
%{_texmfdistdir}/omega/ocp/char2uni/insf1.ocp
%{_texmfdistdir}/omega/ocp/char2uni/insf2.ocp
%{_texmfdistdir}/omega/ocp/char2uni/intis620.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inucode.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inutf8.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inviet1.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inviet2.ocp
%{_texmfdistdir}/omega/ocp/char2uni/inviscii.ocp
%{_texmfdistdir}/omega/ocp/misc/ebcdic.ocp
%{_texmfdistdir}/omega/ocp/misc/id.ocp
%{_texmfdistdir}/omega/ocp/omega/7arb2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7ber2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7cyr2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7hma2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7in88593.ocp
%{_texmfdistdir}/omega/ocp/omega/7lbe2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7pap2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7pas2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7snd2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7syr2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7tbe2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/7urd2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/8mac-arb2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/8mac-cyr2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/apostr2psili.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2acad.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2amal.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2arab.ex.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2arab.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2asv.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2bout.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2mona.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2nar.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2nva.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2oar-novow.ocp
%{_texmfdistdir}/omega/ocp/omega/cuni2oar.ocp
%{_texmfdistdir}/omega/ocp/omega/cunioara.ocp
%{_texmfdistdir}/omega/ocp/omega/dblquote-point.ocp
%{_texmfdistdir}/omega/ocp/omega/destroy.ocp
%{_texmfdistdir}/omega/ocp/omega/french2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/greek.ocp
%{_texmfdistdir}/omega/ocp/omega/grpo2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/grpotilde2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/inverted-iota-upsilon.ocp
%{_texmfdistdir}/omega/ocp/omega/isogr2uni-verbatim.ocp
%{_texmfdistdir}/omega/ocp/omega/isogr2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/lat2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/lowercase.ocp
%{_texmfdistdir}/omega/ocp/omega/lunatesigma.ocp
%{_texmfdistdir}/omega/ocp/omega/macgr2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/medbeta.ocp
%{_texmfdistdir}/omega/ocp/omega/mixedgreek2uni.ocp
%{_texmfdistdir}/omega/ocp/omega/tarauni.ocp
%{_texmfdistdir}/omega/ocp/omega/test1.ocp
%{_texmfdistdir}/omega/ocp/omega/test3.ocp
%{_texmfdistdir}/omega/ocp/omega/tiqwah.ocp
%{_texmfdistdir}/omega/ocp/omega/tiqwah2.ocp
%{_texmfdistdir}/omega/ocp/omega/tsinduni.ocp
%{_texmfdistdir}/omega/ocp/omega/turduuni.ocp
%{_texmfdistdir}/omega/ocp/omega/uni2cuni.ocp
%{_texmfdistdir}/omega/ocp/omega/uni2greek-verbatim.ocp
%{_texmfdistdir}/omega/ocp/omega/uni2greek.ocp
%{_texmfdistdir}/omega/ocp/omega/uni2lat-noffi.ocp
%{_texmfdistdir}/omega/ocp/omega/uni2lat.ocp
%{_texmfdistdir}/omega/ocp/omega/unicuni.ocp
%{_texmfdistdir}/omega/ocp/omega/uppercase-no-accents.ocp
%{_texmfdistdir}/omega/ocp/omega/uppercase.ocp
%{_texmfdistdir}/omega/ocp/uni2char/out88591.ocp
%{_texmfdistdir}/omega/ocp/uni2char/oututf8.ocp
%{_texmfdistdir}/omega/otp/char2uni/in646.otp
%{_texmfdistdir}/omega/otp/char2uni/in88591.otp
%{_texmfdistdir}/omega/otp/char2uni/in88592.otp
%{_texmfdistdir}/omega/otp/char2uni/in88593.otp
%{_texmfdistdir}/omega/otp/char2uni/in88594.otp
%{_texmfdistdir}/omega/otp/char2uni/in88595.otp
%{_texmfdistdir}/omega/otp/char2uni/in88596.otp
%{_texmfdistdir}/omega/otp/char2uni/in88597.otp
%{_texmfdistdir}/omega/otp/char2uni/in88598.otp
%{_texmfdistdir}/omega/otp/char2uni/in88599.otp
%{_texmfdistdir}/omega/otp/char2uni/in8859a.otp
%{_texmfdistdir}/omega/otp/char2uni/in8859d.otp
%{_texmfdistdir}/omega/otp/char2uni/in8859e.otp
%{_texmfdistdir}/omega/otp/char2uni/in8859f.otp
%{_texmfdistdir}/omega/otp/char2uni/in8859g.otp
%{_texmfdistdir}/omega/otp/char2uni/inatari.otp
%{_texmfdistdir}/omega/otp/char2uni/inav.otp
%{_texmfdistdir}/omega/otp/char2uni/inbig5.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1250.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1251.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1252.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1253.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1254.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1255.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1256.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1257.otp
%{_texmfdistdir}/omega/otp/char2uni/incp1258.otp
%{_texmfdistdir}/omega/otp/char2uni/incp866.otp
%{_texmfdistdir}/omega/otp/char2uni/incp874.otp
%{_texmfdistdir}/omega/otp/char2uni/inebcdic.otp
%{_texmfdistdir}/omega/otp/char2uni/ingb.otp
%{_texmfdistdir}/omega/otp/char2uni/inkoi8.otp
%{_texmfdistdir}/omega/otp/char2uni/inmac.otp
%{_texmfdistdir}/omega/otp/char2uni/inmsdos.otp
%{_texmfdistdir}/omega/otp/char2uni/inmsdos2.otp
%{_texmfdistdir}/omega/otp/char2uni/innext.otp
%{_texmfdistdir}/omega/otp/char2uni/inov.otp
%{_texmfdistdir}/omega/otp/char2uni/inps2.otp
%{_texmfdistdir}/omega/otp/char2uni/insf1.otp
%{_texmfdistdir}/omega/otp/char2uni/insf2.otp
%{_texmfdistdir}/omega/otp/char2uni/intis620.otp
%{_texmfdistdir}/omega/otp/char2uni/inucode.otp
%{_texmfdistdir}/omega/otp/char2uni/inutf8.otp
%{_texmfdistdir}/omega/otp/char2uni/inviet1.otp
%{_texmfdistdir}/omega/otp/char2uni/inviet2.otp
%{_texmfdistdir}/omega/otp/char2uni/inviscii.otp
%{_texmfdistdir}/omega/otp/misc/ebcdic.otp
%{_texmfdistdir}/omega/otp/misc/id.otp
%{_texmfdistdir}/omega/otp/omega/7arb2uni.otp
%{_texmfdistdir}/omega/otp/omega/7ber2uni.otp
%{_texmfdistdir}/omega/otp/omega/7cyr2uni.otp
%{_texmfdistdir}/omega/otp/omega/7hma2uni.otp
%{_texmfdistdir}/omega/otp/omega/7in88593.otp
%{_texmfdistdir}/omega/otp/omega/7lbe2uni.otp
%{_texmfdistdir}/omega/otp/omega/7pap2uni.otp
%{_texmfdistdir}/omega/otp/omega/7pas2uni.otp
%{_texmfdistdir}/omega/otp/omega/7snd2uni.otp
%{_texmfdistdir}/omega/otp/omega/7syr2uni.otp
%{_texmfdistdir}/omega/otp/omega/7tbe2uni.otp
%{_texmfdistdir}/omega/otp/omega/7urd2uni.otp
%{_texmfdistdir}/omega/otp/omega/8mac-arb2uni.otp
%{_texmfdistdir}/omega/otp/omega/8mac-cyr2uni.otp
%{_texmfdistdir}/omega/otp/omega/apostr2psili.otp
%{_texmfdistdir}/omega/otp/omega/cuni2acad.otp
%{_texmfdistdir}/omega/otp/omega/cuni2amal.otp
%{_texmfdistdir}/omega/otp/omega/cuni2arab.ex.otp
%{_texmfdistdir}/omega/otp/omega/cuni2asv.otp
%{_texmfdistdir}/omega/otp/omega/cuni2bout.otp
%{_texmfdistdir}/omega/otp/omega/cuni2mona.otp
%{_texmfdistdir}/omega/otp/omega/cuni2nar.otp
%{_texmfdistdir}/omega/otp/omega/cuni2nva.otp
%{_texmfdistdir}/omega/otp/omega/cuni2oar-novow.otp
%{_texmfdistdir}/omega/otp/omega/cuni2oar.otp
%{_texmfdistdir}/omega/otp/omega/dblquote-point.otp
%{_texmfdistdir}/omega/otp/omega/destroy.otp
%{_texmfdistdir}/omega/otp/omega/french2uni.otp
%{_texmfdistdir}/omega/otp/omega/grpo2uni.otp
%{_texmfdistdir}/omega/otp/omega/grpotilde2uni.otp
%{_texmfdistdir}/omega/otp/omega/inverted-iota-upsilon.otp
%{_texmfdistdir}/omega/otp/omega/isogr2uni-verbatim.otp
%{_texmfdistdir}/omega/otp/omega/isogr2uni.otp
%{_texmfdistdir}/omega/otp/omega/lat2uni.otp
%{_texmfdistdir}/omega/otp/omega/lowercase.otp
%{_texmfdistdir}/omega/otp/omega/lunatesigma.otp
%{_texmfdistdir}/omega/otp/omega/macgr2uni.otp
%{_texmfdistdir}/omega/otp/omega/medbeta.otp
%{_texmfdistdir}/omega/otp/omega/mixedgreek2uni.otp
%{_texmfdistdir}/omega/otp/omega/uni2cuni.otp
%{_texmfdistdir}/omega/otp/omega/uni2greek-verbatim.otp
%{_texmfdistdir}/omega/otp/omega/uni2greek.otp
%{_texmfdistdir}/omega/otp/omega/uni2lat-noffi.otp
%{_texmfdistdir}/omega/otp/omega/uni2lat.otp
%{_texmfdistdir}/omega/otp/omega/uppercase-no-accents.otp
%{_texmfdistdir}/omega/otp/omega/uppercase.otp
%{_texmfdistdir}/omega/otp/uni2char/out88591.otp
%{_texmfdistdir}/omega/otp/uni2char/oututf8.otp
%{_texmfdistdir}/tex/generic/encodings/cmbsy.onm
%{_texmfdistdir}/tex/generic/encodings/cmbx.onm
%{_texmfdistdir}/tex/generic/encodings/cmcsc.onm
%{_texmfdistdir}/tex/generic/encodings/cmex.onm
%{_texmfdistdir}/tex/generic/encodings/cmmi.onm
%{_texmfdistdir}/tex/generic/encodings/cmmib.onm
%{_texmfdistdir}/tex/generic/encodings/cmr.onm
%{_texmfdistdir}/tex/generic/encodings/cmr1.onm
%{_texmfdistdir}/tex/generic/encodings/cmsl.onm
%{_texmfdistdir}/tex/generic/encodings/cmsy.onm
%{_texmfdistdir}/tex/generic/encodings/cmti.onm
%{_texmfdistdir}/tex/generic/encodings/cmtt.onm
%{_texmfdistdir}/tex/generic/encodings/ecrm.onm
%{_texmfdistdir}/tex/generic/encodings/euex.onm
%{_texmfdistdir}/tex/generic/encodings/eufb.onm
%{_texmfdistdir}/tex/generic/encodings/eufm.onm
%{_texmfdistdir}/tex/generic/encodings/eurb.onm
%{_texmfdistdir}/tex/generic/encodings/eurm.onm
%{_texmfdistdir}/tex/generic/encodings/eusb.onm
%{_texmfdistdir}/tex/generic/encodings/eusm.onm
%{_texmfdistdir}/tex/generic/encodings/msam.onm
%{_texmfdistdir}/tex/generic/encodings/msbm.onm
%{_texmfdistdir}/tex/generic/omegahyph/bghyph.tex
%{_texmfdistdir}/tex/generic/omegahyph/lthyph.tex
%{_texmfdistdir}/tex/generic/omegahyph/srhyph.tex
%{_texmfdistdir}/tex/plain/omega/grlccode.tex
%{_texmfdistdir}/tex/plain/omega/omega.tex
%doc %{_texmfdistdir}/doc/omega/base/doc-1.8.tex
%doc %{_texmfdistdir}/doc/omega/base/torture.ps
%doc %{_texmfdistdir}/doc/omega/base/torture.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts omega tex doc %{buildroot}%{_texmfdistdir}
