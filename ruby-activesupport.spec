%define	rname	activesupport

Summary:	Support and utility classes used by the Rails framework

Name:		ruby-%{rname}
Version:	4.1.1
Release:	4
URL:		http://as.rubyonrails.com/
Source0:	http://rubygems.org/downloads/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 
Provides:	rubygem(%{rname})
Provides:	rubygem-activesupport

%description
Utility library which carries commonly used classes and goodies from the Rails
framework.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --no-rdoc --no-ri --local --install-dir %{buildroot}/%{gem_dir} --force %{SOURCE0}

rm -rf %{buildroot}%{gem_dir}/cache

%files
%{gem_dir}/gems/%{rname}-%{version}
%{gem_dir}/specifications/%{rname}-%{version}.gemspec


