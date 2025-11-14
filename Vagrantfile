# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|

  if Vagrant.has_plugin? "vagrant-vbguest"
    config.vbguest.no_install = true
    config.vbguest.auto_update = false
    config.vbguest.no_remote = true
  end

  config.vm.define :servidorUbuntu3 do |servidorUbuntu3|
    servidorUbuntu3.vm.box = "bento/ubuntu-22.04"
    servidorUbuntu3.vm.network :private_network, ip: "192.168.100.4"
    servidorUbuntu3.vm.hostname = "servidorUbuntu3"
    servidorUbuntu2.vm.box_download_insecure = true
  end
end
