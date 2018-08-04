
require 'sketchup.rb'

module Lang_Basics2
  module Pyr3
    def self.pyramid
      model = Sketchup.active_model
      model.start_operation('pyramid', true)
      group = model.active_entities.add_group
      entities = group.entities
      scale = (4.to_f)
      h = scale * (Math.sqrt(3) / 2)
      q = scale / 2
      # trying to find x,y of base centroid
      # tried various Math.cos, 2*(h/3), etc; issue is fitting
      # centroid on x,y, not relative to triangle itself
      xx = ?
      yy = ?
      hh = ?
      # 3d location 
      vert = Geom::Point3d.new(xx, yy, hh)
      a = [
      Geom::Point3d.new(0,   0,   0),
      Geom::Point3d.new(scale, 0, 0),
      Geom::Point3d.new(q, h,  0)
      ]
      
      tri = [a[0], a[1], a[2]]
        b = [vert, a[0], a[1]]
        c = [a[2], vert, a[0]]
        d = [a[1], a[2], vert]
      face = entities.add_face(tri)
      face = entities.add_face(b)
      face = entities.add_face(c)
      face = entities.add_face(d)
      model.commit_operation
    end
    unless file_loaded?(__FILE__)
      menu = UI.menu('Plugins')
      menu.add_item('Pyr') {
        self.pyramid
      }
      file_loaded(__FILE__)
    end
  end # module Pyr
end # mod Lang_Basics
