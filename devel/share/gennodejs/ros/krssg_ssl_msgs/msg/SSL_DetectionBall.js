// Auto-generated. Do not edit!

// (in-package krssg_ssl_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class SSL_DetectionBall {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.confidence = null;
      this.area = null;
      this.x = null;
      this.y = null;
      this.z = null;
      this.pixel_x = null;
      this.pixel_y = null;
    }
    else {
      if (initObj.hasOwnProperty('confidence')) {
        this.confidence = initObj.confidence
      }
      else {
        this.confidence = 0.0;
      }
      if (initObj.hasOwnProperty('area')) {
        this.area = initObj.area
      }
      else {
        this.area = 0;
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
      if (initObj.hasOwnProperty('z')) {
        this.z = initObj.z
      }
      else {
        this.z = 0.0;
      }
      if (initObj.hasOwnProperty('pixel_x')) {
        this.pixel_x = initObj.pixel_x
      }
      else {
        this.pixel_x = 0.0;
      }
      if (initObj.hasOwnProperty('pixel_y')) {
        this.pixel_y = initObj.pixel_y
      }
      else {
        this.pixel_y = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SSL_DetectionBall
    // Serialize message field [confidence]
    bufferOffset = _serializer.float64(obj.confidence, buffer, bufferOffset);
    // Serialize message field [area]
    bufferOffset = _serializer.uint32(obj.area, buffer, bufferOffset);
    // Serialize message field [x]
    bufferOffset = _serializer.float64(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float64(obj.y, buffer, bufferOffset);
    // Serialize message field [z]
    bufferOffset = _serializer.float64(obj.z, buffer, bufferOffset);
    // Serialize message field [pixel_x]
    bufferOffset = _serializer.float64(obj.pixel_x, buffer, bufferOffset);
    // Serialize message field [pixel_y]
    bufferOffset = _serializer.float64(obj.pixel_y, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SSL_DetectionBall
    let len;
    let data = new SSL_DetectionBall(null);
    // Deserialize message field [confidence]
    data.confidence = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [area]
    data.area = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [x]
    data.x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [z]
    data.z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pixel_x]
    data.pixel_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pixel_y]
    data.pixel_y = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 52;
  }

  static datatype() {
    // Returns string type for a message object
    return 'krssg_ssl_msgs/SSL_DetectionBall';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'da53de0da1e4e3e19a8eddfe942e84c8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64  confidence 
    uint32 area      
    float64  x         
    float64  y          
    float64  z          
    float64  pixel_x    
    float64  pixel_y    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SSL_DetectionBall(null);
    if (msg.confidence !== undefined) {
      resolved.confidence = msg.confidence;
    }
    else {
      resolved.confidence = 0.0
    }

    if (msg.area !== undefined) {
      resolved.area = msg.area;
    }
    else {
      resolved.area = 0
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    if (msg.z !== undefined) {
      resolved.z = msg.z;
    }
    else {
      resolved.z = 0.0
    }

    if (msg.pixel_x !== undefined) {
      resolved.pixel_x = msg.pixel_x;
    }
    else {
      resolved.pixel_x = 0.0
    }

    if (msg.pixel_y !== undefined) {
      resolved.pixel_y = msg.pixel_y;
    }
    else {
      resolved.pixel_y = 0.0
    }

    return resolved;
    }
};

module.exports = SSL_DetectionBall;
