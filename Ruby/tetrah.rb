
require 'sketchup.rb'

module Lang_Basics
  module Pyr4
    def self.pyramid
      model = Sketchup.active_model
      model.start_operation('pyramid', true)
      group = model.active_entities.add_group
      entities = group.entities
      # scale should, (ideally) change the size of the whole triangle
      # if it is changed
      scale = (4.to_f)
        a = Geom::Point3d.new(scale, 0, 0)
        b = Geom::Point3d.new(0, scale,  0)
        c = Geom::Point3d.new(0, 0,  scale)
        d = Geom::Point3d.new(scale, scale, scale)
      face = entities.add_face(a,b,c)
      face = entities.add_face(b,c,d)
      face = entities.add_face(c,d,a)
      face = entities.add_face(d,a,b)
    end
    unless file_loaded?(__FILE__)
      menu = UI.menu('Plugins')
      menu.add_item('Tetrah') {
        self.pyramid
      }
      file_loaded(__FILE__)
    end
  end # module Pyr4
end # Lang_Basics

