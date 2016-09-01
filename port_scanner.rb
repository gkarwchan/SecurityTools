#!/usr/bin/ruby

require 'socket'

def scanner(h, p)
    sock = Socket.new(:INET, :STREAM)
    raw = Socket.sockaddr_in(p, h)
    puts "#{p} open." if sock.connect(raw)


