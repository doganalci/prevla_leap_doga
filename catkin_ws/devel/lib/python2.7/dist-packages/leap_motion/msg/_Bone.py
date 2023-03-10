# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from leap_motion/Bone.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class Bone(genpy.Message):
  _md5sum = "ce39afad61bdb16ab802b0100be50795"
  _type = "leap_motion/Bone"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header

# The name of this bone. 
uint8 type

# The estimated length of the bone in meters.
float32 length

# The estimated with of the bone in meters.
float32 width

# A string containing a brief, human readable description of the Bone object. 
string to_string

# The base of the bone, closest to the wrist. 
geometry_msgs/Pose bone_start

# The end of the bone, closest to the finger tip. 
geometry_msgs/Pose bone_end

# The midpoint of the bone. 
float32[] center

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','type','length','width','to_string','bone_start','bone_end','center']
  _slot_types = ['std_msgs/Header','uint8','float32','float32','string','geometry_msgs/Pose','geometry_msgs/Pose','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,type,length,width,to_string,bone_start,bone_end,center

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Bone, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.type is None:
        self.type = 0
      if self.length is None:
        self.length = 0.
      if self.width is None:
        self.width = 0.
      if self.to_string is None:
        self.to_string = ''
      if self.bone_start is None:
        self.bone_start = geometry_msgs.msg.Pose()
      if self.bone_end is None:
        self.bone_end = geometry_msgs.msg.Pose()
      if self.center is None:
        self.center = []
    else:
      self.header = std_msgs.msg.Header()
      self.type = 0
      self.length = 0.
      self.width = 0.
      self.to_string = ''
      self.bone_start = geometry_msgs.msg.Pose()
      self.bone_end = geometry_msgs.msg.Pose()
      self.center = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B2f().pack(_x.type, _x.length, _x.width))
      _x = self.to_string
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_14d().pack(_x.bone_start.position.x, _x.bone_start.position.y, _x.bone_start.position.z, _x.bone_start.orientation.x, _x.bone_start.orientation.y, _x.bone_start.orientation.z, _x.bone_start.orientation.w, _x.bone_end.position.x, _x.bone_end.position.y, _x.bone_end.position.z, _x.bone_end.orientation.x, _x.bone_end.orientation.y, _x.bone_end.orientation.z, _x.bone_end.orientation.w))
      length = len(self.center)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.center))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.bone_start is None:
        self.bone_start = geometry_msgs.msg.Pose()
      if self.bone_end is None:
        self.bone_end = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.type, _x.length, _x.width,) = _get_struct_B2f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.to_string = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.to_string = str[start:end]
      _x = self
      start = end
      end += 112
      (_x.bone_start.position.x, _x.bone_start.position.y, _x.bone_start.position.z, _x.bone_start.orientation.x, _x.bone_start.orientation.y, _x.bone_start.orientation.z, _x.bone_start.orientation.w, _x.bone_end.position.x, _x.bone_end.position.y, _x.bone_end.position.z, _x.bone_end.orientation.x, _x.bone_end.orientation.y, _x.bone_end.orientation.z, _x.bone_end.orientation.w,) = _get_struct_14d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.center = s.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B2f().pack(_x.type, _x.length, _x.width))
      _x = self.to_string
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_14d().pack(_x.bone_start.position.x, _x.bone_start.position.y, _x.bone_start.position.z, _x.bone_start.orientation.x, _x.bone_start.orientation.y, _x.bone_start.orientation.z, _x.bone_start.orientation.w, _x.bone_end.position.x, _x.bone_end.position.y, _x.bone_end.position.z, _x.bone_end.orientation.x, _x.bone_end.orientation.y, _x.bone_end.orientation.z, _x.bone_end.orientation.w))
      length = len(self.center)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.center.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.bone_start is None:
        self.bone_start = geometry_msgs.msg.Pose()
      if self.bone_end is None:
        self.bone_end = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.type, _x.length, _x.width,) = _get_struct_B2f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.to_string = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.to_string = str[start:end]
      _x = self
      start = end
      end += 112
      (_x.bone_start.position.x, _x.bone_start.position.y, _x.bone_start.position.z, _x.bone_start.orientation.x, _x.bone_start.orientation.y, _x.bone_start.orientation.z, _x.bone_start.orientation.w, _x.bone_end.position.x, _x.bone_end.position.y, _x.bone_end.position.z, _x.bone_end.orientation.x, _x.bone_end.orientation.y, _x.bone_end.orientation.z, _x.bone_end.orientation.w,) = _get_struct_14d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.center = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_14d = None
def _get_struct_14d():
    global _struct_14d
    if _struct_14d is None:
        _struct_14d = struct.Struct("<14d")
    return _struct_14d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B2f = None
def _get_struct_B2f():
    global _struct_B2f
    if _struct_B2f is None:
        _struct_B2f = struct.Struct("<B2f")
    return _struct_B2f
