#
# Created by Luis Vera
#

import streamlit as st

st.set_page_config(
    page_title="SWP",
    layout='wide'
)

# ----- Body ----- #

st.markdown("# FAQ")
st.write("Bleow are a few FAQs that may help you further your understanding of Strategic Workforce Planning (SWP).")

with st.expander("What is SWP?"):
    st.write(
        """
        SWP, or Strategic Workforce Planning, can be defined in many ways. Some describe it simply as “having the right person, at the right time, with the right skill sets.” Others offer more detailed explanations. For me, SWP is an ongoing optimization process that focuses on aligning talent strategies with future growth needs.
        """
)
 
with st.expander("When should an organization use SWP?"):
    st.write(
        """
        An organization should use Strategic Workforce Planning (SWP) continually. It's not a one-time initiative but an ongoing optimization process that needs to be regularly revised, updated, and even revamped. As business needs, market conditions, and talent landscapes evolve, SWP ensures that the organization remains agile and well-prepared for future growth by constantly realigning talent strategies.
        """
)
    
with st.expander("Who should use SWP?"):
    st.write(
        """
        This is debatable. Some believe SWP is only for people managers, but I’m in the camp that believes it’s valuable for anyone involved in understanding workforce planning concepts. Whether you’re a manager or not, if you’re running scenarios and analyzing workforce strategies, you’re contributing to the organization’s success. SWP is most effective when embraced across all levels, not just by those in leadership roles.
        """
)
    
with st.expander("How does an organization use SWP?"):
    st.write(
        """
        SWP is both a tool and a practice for those involved in making strategic decisions. It works best when organizations hold regular meetings to review, update, and refine their workforce plan. This continual review process is especially valuable for companies with high-growth plans, as it ensures the organization remains agile and prepared for future talent needs. 
        """
)
    
with st.expander("Why would an organization use SWP?"):
    st.write(
        """
        Today, from start-ups to mature companies, organizations are constantly competing for the best talent strategies. As data and technology continue to transform outdated HR methodologies, staying agile and at the forefront of strategic thinking becomes essential. SWP helps organizations achieve this by enabling them to proactively plan for future talent needs and stay competitive in a rapidly evolving landscape.
        """
)
