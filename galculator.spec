%define name galculator 
%define version 1.3.1
%define release %mkrel 4

Name: %{name}
Summary: GTK 2 based calculator
Version: %{version}
Release: %{release}
Source: http://prdownloads.sourceforge.net/galculator/%{name}-%{version}.tar.bz2
Patch0: galculator-1.3.1-fix-desktop.patch
URL: http://galculator.sourceforge.net/
Group: Office
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License: GPLv2+
BuildRequires: libglade2.0-devel
BuildRequires: ImageMagick

%description
Galculator is a calculator that features two user modes: basic and
scientific mode.  Basic mode is intended for simple computations.
Only the most important operations and functions are available in
algebraic mode as well as in Reverse Polish Mode.

%prep 
%setup -q
%patch0 -p0

%build 
%configure2_5x 
%make

%install
rm -fr %buildroot 
%makeinstall_std

mkdir -p %buildroot/{%_iconsdir,%_miconsdir,%_liconsdir}
convert -resize 16x16 pixmaps/galculator_48x48.png %buildroot%_miconsdir/%name.png
convert -resize 32x16 pixmaps/galculator_48x48.png %buildroot%_iconsdir/%name.png
cp pixmaps/galculator_48x48.png %buildroot%_liconsdir/%name.png

%find_lang  %{name}

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS README THANKS TODO ChangeLog doc/shortcuts
%{_bindir}/galculator
%{_datadir}/galculator
%{_mandir}/man1/galculator.1.*
%{_datadir}/applications/galculator.desktop
%{_miconsdir}/%name.png
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_datadir}/pixmaps/galculator
