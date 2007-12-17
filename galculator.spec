%define name galculator 
%define version 1.2.5.2
%define release %mkrel 2

Name: %{name} 
Summary: Galculator is a GTK 2 based calculator 
Version: %{version} 
Release: %{release} 
Source: http://prdownloads.sourceforge.net/galculator/%{name}-%{version}.tar.bz2 
Source1: gcalc-icons.tar.bz2
URL: http://galculator.sourceforge.net/ 
Group: Office 
License: GPL
BuildRequires: libglade2.0-devel
BuildRequires: desktop-file-utils

%description
Galculator is a calculator that features two user modes: basic and
scientific mode.  Basic mode is intended for simple computations.
Only the most important operations and functions are available in
algebraic mode as well as in Reverse Polish Mode.

%prep 
rm -rf $RPM_BUILD_ROOT

%setup -q 
tar xjf %{SOURCE1}

%build 
%configure2_5x 
%make

%install 
%makeinstall

# Menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="Utility" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p %buildroot/%_iconsdir
cp -a gcalc.png mini large %buildroot/%_iconsdir

%find_lang  %{name}
%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%{_bindir}/galculator
%{_datadir}/galculator/*
%dir %{_datadir}/galculator
%{_mandir}/man1/galculator.1.*
%{_datadir}/applications/galculator.desktop
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS README THANKS TODO ChangeLog doc/shortcuts
%{_miconsdir}/gcalc.png
%{_iconsdir}/gcalc.png
%{_liconsdir}/gcalc.png


