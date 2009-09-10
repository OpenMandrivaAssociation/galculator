%define name galculator 
%define version 1.3.4
%define release %mkrel 2

Name: %{name}
Summary: GTK 2 based calculator
Version: %{version}
Release: %{release}
Source: http://prdownloads.sourceforge.net/galculator/%{name}-%{version}.tar.bz2
URL: http://galculator.sourceforge.net/
Group: Office
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License: GPLv2+
BuildRequires: libglade2.0-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils

%description
Galculator is a calculator that features two user modes: basic and
scientific mode.  Basic mode is intended for simple computations.
Only the most important operations and functions are available in
algebraic mode as well as in Reverse Polish Mode.

%prep 
%setup -q

%build 
%configure2_5x 
%make

%install
rm -fr %buildroot 
%makeinstall_std

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--add-category='Calculator;GTK;GNOME' \
	%buildroot%_datadir/applications/*.desktop

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
%{_datadir}/pixmaps/*
