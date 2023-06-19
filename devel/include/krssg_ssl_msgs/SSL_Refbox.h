// Generated by gencpp from file krssg_ssl_msgs/SSL_Refbox.msg
// DO NOT EDIT!


#ifndef KRSSG_SSL_MSGS_MESSAGE_SSL_REFBOX_H
#define KRSSG_SSL_MSGS_MESSAGE_SSL_REFBOX_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace krssg_ssl_msgs
{
template <class ContainerAllocator>
struct SSL_Refbox_
{
  typedef SSL_Refbox_<ContainerAllocator> Type;

  SSL_Refbox_()
    : packet_timestamp(0.0)
    , stage(0)
    , stage_time_left(0)
    , command(0)
    , command_counter(0)
    , command_timestamp(0)
    , b_name()
    , b_score(0)
    , b_red_cards(0)
    , b_yellow_cards(0)
    , b_timeouts(0)
    , b_timeout_time(0)
    , b_goalie(0)
    , y_name()
    , y_score(0)
    , y_red_cards(0)
    , y_yellow_cards(0)
    , y_timeouts(0)
    , y_timeout_time(0)
    , y_goalie(0)
    , y_card_times()
    , b_card_times()  {
    }
  SSL_Refbox_(const ContainerAllocator& _alloc)
    : packet_timestamp(0.0)
    , stage(0)
    , stage_time_left(0)
    , command(0)
    , command_counter(0)
    , command_timestamp(0)
    , b_name(_alloc)
    , b_score(0)
    , b_red_cards(0)
    , b_yellow_cards(0)
    , b_timeouts(0)
    , b_timeout_time(0)
    , b_goalie(0)
    , y_name(_alloc)
    , y_score(0)
    , y_red_cards(0)
    , y_yellow_cards(0)
    , y_timeouts(0)
    , y_timeout_time(0)
    , y_goalie(0)
    , y_card_times(_alloc)
    , b_card_times(_alloc)  {
  (void)_alloc;
    }



   typedef double _packet_timestamp_type;
  _packet_timestamp_type packet_timestamp;

   typedef uint32_t _stage_type;
  _stage_type stage;

   typedef uint32_t _stage_time_left_type;
  _stage_time_left_type stage_time_left;

   typedef uint32_t _command_type;
  _command_type command;

   typedef uint32_t _command_counter_type;
  _command_counter_type command_counter;

   typedef uint32_t _command_timestamp_type;
  _command_timestamp_type command_timestamp;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _b_name_type;
  _b_name_type b_name;

   typedef uint32_t _b_score_type;
  _b_score_type b_score;

   typedef uint32_t _b_red_cards_type;
  _b_red_cards_type b_red_cards;

   typedef uint32_t _b_yellow_cards_type;
  _b_yellow_cards_type b_yellow_cards;

   typedef uint32_t _b_timeouts_type;
  _b_timeouts_type b_timeouts;

   typedef uint32_t _b_timeout_time_type;
  _b_timeout_time_type b_timeout_time;

   typedef uint32_t _b_goalie_type;
  _b_goalie_type b_goalie;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _y_name_type;
  _y_name_type y_name;

   typedef uint32_t _y_score_type;
  _y_score_type y_score;

   typedef uint32_t _y_red_cards_type;
  _y_red_cards_type y_red_cards;

   typedef uint32_t _y_yellow_cards_type;
  _y_yellow_cards_type y_yellow_cards;

   typedef uint32_t _y_timeouts_type;
  _y_timeouts_type y_timeouts;

   typedef uint32_t _y_timeout_time_type;
  _y_timeout_time_type y_timeout_time;

   typedef uint32_t _y_goalie_type;
  _y_goalie_type y_goalie;

   typedef std::vector<uint32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint32_t>> _y_card_times_type;
  _y_card_times_type y_card_times;

   typedef std::vector<uint32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint32_t>> _b_card_times_type;
  _b_card_times_type b_card_times;





  typedef boost::shared_ptr< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> const> ConstPtr;

}; // struct SSL_Refbox_

typedef ::krssg_ssl_msgs::SSL_Refbox_<std::allocator<void> > SSL_Refbox;

typedef boost::shared_ptr< ::krssg_ssl_msgs::SSL_Refbox > SSL_RefboxPtr;
typedef boost::shared_ptr< ::krssg_ssl_msgs::SSL_Refbox const> SSL_RefboxConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator1> & lhs, const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator2> & rhs)
{
  return lhs.packet_timestamp == rhs.packet_timestamp &&
    lhs.stage == rhs.stage &&
    lhs.stage_time_left == rhs.stage_time_left &&
    lhs.command == rhs.command &&
    lhs.command_counter == rhs.command_counter &&
    lhs.command_timestamp == rhs.command_timestamp &&
    lhs.b_name == rhs.b_name &&
    lhs.b_score == rhs.b_score &&
    lhs.b_red_cards == rhs.b_red_cards &&
    lhs.b_yellow_cards == rhs.b_yellow_cards &&
    lhs.b_timeouts == rhs.b_timeouts &&
    lhs.b_timeout_time == rhs.b_timeout_time &&
    lhs.b_goalie == rhs.b_goalie &&
    lhs.y_name == rhs.y_name &&
    lhs.y_score == rhs.y_score &&
    lhs.y_red_cards == rhs.y_red_cards &&
    lhs.y_yellow_cards == rhs.y_yellow_cards &&
    lhs.y_timeouts == rhs.y_timeouts &&
    lhs.y_timeout_time == rhs.y_timeout_time &&
    lhs.y_goalie == rhs.y_goalie &&
    lhs.y_card_times == rhs.y_card_times &&
    lhs.b_card_times == rhs.b_card_times;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator1> & lhs, const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace krssg_ssl_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "473e87105d23511aae7f9b0fe64666df";
  }

  static const char* value(const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x473e87105d23511aULL;
  static const uint64_t static_value2 = 0xae7f9b0fe64666dfULL;
};

template<class ContainerAllocator>
struct DataType< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "krssg_ssl_msgs/SSL_Refbox";
  }

  static const char* value(const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 packet_timestamp\n"
"uint32 stage\n"
"uint32 stage_time_left\n"
"uint32 command\n"
"uint32 command_counter\n"
"uint32 command_timestamp\n"
"string b_name\n"
"uint32 b_score\n"
"uint32 b_red_cards\n"
"uint32 b_yellow_cards\n"
"uint32 b_timeouts\n"
"uint32 b_timeout_time\n"
"uint32 b_goalie\n"
"string y_name\n"
"uint32 y_score\n"
"uint32 y_red_cards\n"
"uint32 y_yellow_cards\n"
"uint32 y_timeouts\n"
"uint32 y_timeout_time\n"
"uint32 y_goalie\n"
"uint32[] y_card_times\n"
"uint32[] b_card_times\n"
"\n"
"	\n"
;
  }

  static const char* value(const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.packet_timestamp);
      stream.next(m.stage);
      stream.next(m.stage_time_left);
      stream.next(m.command);
      stream.next(m.command_counter);
      stream.next(m.command_timestamp);
      stream.next(m.b_name);
      stream.next(m.b_score);
      stream.next(m.b_red_cards);
      stream.next(m.b_yellow_cards);
      stream.next(m.b_timeouts);
      stream.next(m.b_timeout_time);
      stream.next(m.b_goalie);
      stream.next(m.y_name);
      stream.next(m.y_score);
      stream.next(m.y_red_cards);
      stream.next(m.y_yellow_cards);
      stream.next(m.y_timeouts);
      stream.next(m.y_timeout_time);
      stream.next(m.y_goalie);
      stream.next(m.y_card_times);
      stream.next(m.b_card_times);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SSL_Refbox_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::krssg_ssl_msgs::SSL_Refbox_<ContainerAllocator>& v)
  {
    s << indent << "packet_timestamp: ";
    Printer<double>::stream(s, indent + "  ", v.packet_timestamp);
    s << indent << "stage: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.stage);
    s << indent << "stage_time_left: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.stage_time_left);
    s << indent << "command: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.command);
    s << indent << "command_counter: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.command_counter);
    s << indent << "command_timestamp: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.command_timestamp);
    s << indent << "b_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.b_name);
    s << indent << "b_score: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.b_score);
    s << indent << "b_red_cards: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.b_red_cards);
    s << indent << "b_yellow_cards: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.b_yellow_cards);
    s << indent << "b_timeouts: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.b_timeouts);
    s << indent << "b_timeout_time: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.b_timeout_time);
    s << indent << "b_goalie: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.b_goalie);
    s << indent << "y_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.y_name);
    s << indent << "y_score: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y_score);
    s << indent << "y_red_cards: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y_red_cards);
    s << indent << "y_yellow_cards: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y_yellow_cards);
    s << indent << "y_timeouts: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y_timeouts);
    s << indent << "y_timeout_time: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y_timeout_time);
    s << indent << "y_goalie: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.y_goalie);
    s << indent << "y_card_times[]" << std::endl;
    for (size_t i = 0; i < v.y_card_times.size(); ++i)
    {
      s << indent << "  y_card_times[" << i << "]: ";
      Printer<uint32_t>::stream(s, indent + "  ", v.y_card_times[i]);
    }
    s << indent << "b_card_times[]" << std::endl;
    for (size_t i = 0; i < v.b_card_times.size(); ++i)
    {
      s << indent << "  b_card_times[" << i << "]: ";
      Printer<uint32_t>::stream(s, indent + "  ", v.b_card_times[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // KRSSG_SSL_MSGS_MESSAGE_SSL_REFBOX_H