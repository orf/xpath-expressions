def test_root_node(xml_doc, xml_root):
    assert xml_doc.xpath(str(xml_root.name)) == "root"


def test_root_node_attr(xml_doc, xml_root):
    res = xml_doc.xpath(str(xml_root.attributes))
    assert len(res) == 1


def test_root_node_children(xml_doc, xml_root):
    children = xml_doc.xpath(str(xml_root.children))
    assert len(children) == 2

    for child in xml_root.children(2):
        assert xml_doc.xpath(str(child))
