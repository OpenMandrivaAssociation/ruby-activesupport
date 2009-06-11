%define rname activesupport
%define name ruby-%{rname}
%define version 2.1.2
%define release %mkrel 1

Summary:	Support and utility classes used by the Rails framework
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://ar.rubyonrails.com/
Source0:	%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	ruby
BuildRequires:	ruby-RubyGems 

%description
Utility library which carries commonly used classes and goodies from the Rails
framework.

%prep
rm -rf %rname-%version
rm -rf tmp-%rname-%version
mkdir tmp-%rname-%version
gem install --ignore-dependencies %{SOURCE0} --no-rdoc --install-dir `pwd`/tmp-%rname-%version
mv tmp-%rname-%version/gems/%rname-%version .
mv tmp-%rname-%version/specifications/%rname-%version.gemspec %rname-%version/
rm -rf tmp-%rname-%version/gems
%setup -T -D -n %rname-%version

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT{%{ruby_sitelibdir},%{ruby_ridir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_sitelibdir}
cp -a ri/ActiveSupport $RPM_BUILD_ROOT%{ruby_ridir}
install -D -m 644 %rname-%version.gemspec $RPM_BUILD_ROOT%{ruby_gemdir}/specifications/%rname-%version.gemspec

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/*
%{ruby_ridir}/*
%{ruby_gemdir}/specifications/%rname-%version.gemspec
%doc CHANGELOG rdoc

