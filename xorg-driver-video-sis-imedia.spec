Summary:	X.org video driver for SiS 671 video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych SiS 671
Name:		xorg-driver-video-sis-imedia
Version:	20080630
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://www.linuxconsulting.ro/xorg-drivers/src/xf86-video-sis-imedia.tgz
# Source0-md5:	0d1a2504af6580236f5fee2d7cfaf3a4
URL:		http://www.linuxconsulting.ro/xorg-drivers/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
#%%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Driver for SIS 671 found in Intel D201GLY, it fixes high resolution
problems, adds 2D hardware acceleration and XV/XVMC support. It
requires a kernel patch to add SIS 671 PCI ids (0x0671) and a new
entry on sis-agp.c to detect the chipset.


%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych SiS 671. Obsługuje
rozne rozdzielczosci, akcelaracje 2D i XV/XVMC. Wymaga latki na kernel
dodajacej pci id dla SiS 671 (ox0671) i wpis w sis-agp.c co pozwala
wykryc uklad.


%prep
%setup -q -n xf86-video-sis-imedia

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.4*
