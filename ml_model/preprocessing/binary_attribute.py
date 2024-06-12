import dask.dataframe as dd
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer, SimpleImputer

from dask.diagnostics.progress import ProgressBar
ProgressBar().register()


def binary_encode1(value):
    if value == "?":
        return 1
    else:
        return 0
    
def binary_encode2(value):
    if value == "0":
        return 1
    else:
        return 0
    
def binary_encode3(value):
    if value == "0x00000000":
        return 1
    else:
        return 0
    
def binary_encode4(value):
    if value == "1-0-0":
        return 1
    else:
        return 0
    
def binary_encode5(value):
    if value == "5":
        return 1
    else:
        return 0
    
def binary_encode6(value):
    if value == "56":
        return 1
    else:
        return 0

def binary_encode7(value):
    if value == "6":
        return 1
    else:
        return 0
    
def binary_encode8(value):
    if value == "86":
        return 1
    else:
        return 0

def binary_encode9(value: str):
    return -1 * int(value.split("-")[1])

def binary_encode10(value):
    if value == "Deauth":
        return 1
    else:
        return 0
    


c1 = [
"arp",
"data.len",
"tcp.ack",
"tcp.ack_raw",
"tcp.checksum",
"tcp.checksum.status",
"tcp.seq",
"tcp.seq_raw",
"tcp.srcport",
"tcp.time_delta",
"tcp.time_relative",
"udp.length",
"udp.time_relative",
"udp.time_delta",
"dns.time",
"wlan.tag.length",
"wlan.ssid",]

c2 = [
    "wlan.fc.frag",
"wlan.fc.order",
"wlan.fc.moredata",
"wlan.fc.protected",
"wlan.fc.pwrmgt",
"wlan.fc.type",
]

c3 = [
    "wlan.fc.ds"
]
c4 = [
    "radiotap.present.tsft"
]
c5 = [
    "wlan_radio.phy"
]
c6 = [
    "radiotap.length"
]
c7 = [
    "radiotap.datarate",
    "wlan_radio.data_rate",
]
c8 = [
    "frame.len"
]
c9 = [
    "radiotap.dbm_antsignal"
]
c10 = [
    "Label"
]



import dask.dataframe as dd

from tqdm import tqdm

def encode_binary(df):
    for c in tqdm(c1):
        df[c] = df[c].apply(binary_encode1, meta=(c, int))
    for c in tqdm(c2):
        df[c] = df[c].apply(binary_encode2, meta=(c, int))
    for c in tqdm(c3):
        df[c] = df[c].apply(binary_encode3, meta=(c, int))
    for c in tqdm(c4):
        df[c] = df[c].apply(binary_encode4, meta=(c, int))
    for c in tqdm(c5):
        df[c] = df[c].apply(binary_encode5, meta=(c, int))
    for c in tqdm(c6):
        df[c] = df[c].apply(binary_encode6, meta=(c, int))
    for c in tqdm(c7):
        df[c] = df[c].apply(binary_encode7, meta=(c, int))
    for c in tqdm(c8):
        df[c] = df[c].apply(binary_encode8, meta=(c, int))
    for c in tqdm(c9):
        df[c] = df[c].apply(binary_encode9, meta=(c, int))
    for c in tqdm(c10):
        df[c] = df[c].apply(binary_encode10, meta=(c, int))

    return df



def fill_missing(df):
    # Replace "?" with Dask's missing value indicator (usually "NA")
    df = df.replace('?', np.nan)

    # Fill "radiotap.mactime" with mean using Dask methods
    mean_value = df['radiotap.mactime'].astype(float).mean().compute()
    df['radiotap.mactime'] = df['radiotap.mactime'].fillna(str(mean_value).split(".")[0])



    # Use SimpleImputer for other columns (avoid KNN for Dask)
    for column in ['wlan_radio.end_tsf', 'wlan_radio.start_tsf', 'wlan_radio.timestamp']:
        non_missing = df[~df[column].isnull()]
        mean = non_missing[column].astype(float).mean().compute()
        df[column] = df[column].fillna((str(mean).split("."))[0])

        # aux = pd.to_numeric(df[column], errors='coerce') 
        # df[column] = df.compute()
        # df[column] = df[column].apply(pd.to_numeric, errors='coerce') 

        # df[column] = dd.from_array(df[[column]].interpolate())
    return df

    

dtypes_categorical = {
    "frame.encap_type": "string",
    "frame.len": "category",
    "frame.number": "string",
    "frame.time": "string",
    "frame.time_delta": "string",
    "frame.time_delta_displayed": "string",
    "frame.time_epoch": "string",
    "frame.time_relative": "string",
    "radiotap.channel.flags.cck": "string",
    "radiotap.channel.flags.ofdm": "string",
    "radiotap.channel.freq": "string",
    "radiotap.datarate": "category",
    "radiotap.dbm_antsignal": "string",
    "radiotap.length": "category",
    "radiotap.mactime": "string",
    "radiotap.present.tsft": "category",
    "radiotap.rxflags": "string",
    "radiotap.timestamp.ts": "string",
    "radiotap.vendor_oui": "string",
    "wlan.duration": "string",
    "wlan.analysis.kck": "string",
    "wlan.analysis.kek": "string",
    "wlan.bssid": "string",
    "wlan.country_info.fnm": "string",
    "wlan.country_info.code": "string",
    "wlan.da": "string",
    "wlan.fc.ds": "category",
    "wlan.fc.frag": "category",
    "wlan.fc.order": "category",
    "wlan.fc.moredata": "category",
    "wlan.fc.protected": "category",
    "wlan.fc.pwrmgt": "category",
    "wlan.fc.type": "category",
    "wlan.fc.retry": "string",
    "wlan.fc.subtype": "string",
    "wlan.fcs.bad_checksum": "string",
    "wlan.fixed.beacon": "string",
    "wlan.fixed.capabilities.ess": "string",
    "wlan.fixed.capabilities.ibss": "string",
    "wlan.fixed.reason_code": "string",
    "wlan.fixed.timestamp": "string",
    "wlan.ra": "string",
    "wlan_radio.duration": "string",
    "wlan.rsn.ie.gtk.key": "string",
    "wlan.rsn.ie.igtk.key": "string",
    "wlan.rsn.ie.pmkid": "string",
    "wlan.sa": "string",
    "wlan.seq": "string",
    "wlan.ssid": "category",
    "wlan.ta": "string",
    "wlan.tag": "string",
    "wlan.tag.length": "category",
    "wlan_radio.channel": "string",
    "wlan_radio.data_rate": "category",
    "wlan_radio.end_tsf": "string",
    "wlan_radio.frequency": "string",
    "wlan_radio.signal_dbm": "string",
    "wlan_radio.start_tsf": "string",
    "wlan_radio.phy": "category",
    "wlan_radio.timestamp": "string",
    "wlan.rsn.capabilities.mfpc": "string",
    "wlan_rsna_eapol.keydes.msgnr": "string",
    "wlan_rsna_eapol.keydes.data": "string",
    "wlan_rsna_eapol.keydes.data_len": "string",
    "wlan_rsna_eapol.keydes.key_info.key_mic": "string",
    "wlan_rsna_eapol.keydes.nonce": "string",
    "eapol.keydes.key_len": "string",
    "eapol.keydes.replay_counter": "string",
    "eapol.len": "string",
    "eapol.type": "string",
    "llc": "string",
    "arp": "category",
    "arp.hw.type": "string",
    "arp.proto.type": "string",
    "arp.hw.size": "string",
    "arp.proto.size": "string",
    "arp.opcode": "string",
    "arp.src.hw_mac": "string",
    "arp.src.proto_ipv4": "string",
    "arp.dst.hw_mac": "string",
    "arp.dst.proto_ipv4": "string",
    "ip.dst": "string",
    "ip.proto": "string",
    "ip.src": "string",
    "ip.ttl": "string",
    "ip.version": "string",
    "data.data": "string",
    "data.len": "category",
    "icmpv6.mldr.nb_mcast_records": "string",
    "icmpv6.ni.nonce": "string",
    "tcp.ack": "category",
    "tcp.ack_raw": "category",
    "tcp.analysis": "string",
    "tcp.analysis.flags": "string",
    "tcp.analysis.retransmission": "string",
    "tcp.analysis.reused_ports": "string",
    "tcp.analysis.rto_frame": "string",
    "tcp.checksum": "category",
    "tcp.checksum.status": "category",
    "tcp.flags.syn": "string",
    "tcp.dstport": "string",
    "tcp.flags.ack": "string",
    "tcp.flags.fin": "string",
    "tcp.flags.push": "string",
    "tcp.flags.reset": "string",
    "tcp.option_len": "string",
    "tcp.payload": "string",
    "tcp.seq": "category",
    "tcp.seq_raw": "category",
    "tcp.srcport": "category",
    "tcp.time_delta": "category",
    "tcp.time_relative": "category",
    "udp.dstport": "string",
    "udp.srcport": "string",
    "udp.length": "category",
    "udp.payload": "string",
    "udp.time_relative": "category",
    "udp.time_delta": "category",
    "nbns": "string",
    "nbss.continuation_data": "string",
    "nbss.type": "string",
    "nbss.length": "string",
    "ldap": "string",
    "smb.access.generic_execute": "string",
    "smb.access.generic_read": "string",
    "smb.access.generic_write": "string",
    "smb.flags.notify": "string",
    "smb.flags.response": "string",
    "smb.flags2.nt_error": "string",
    "smb.flags2.sec_sig": "string",
    "smb.mid": "string",
    "smb.nt_status": "string",
    "smb.server_component": "string",
    "smb.pid.high": "string",
    "smb.tid": "string",
    "smb2.acct": "string",
    "smb2.auth_frame": "string",
    "smb2.buffer_code": "string",
    "smb2.cmd": "string",
    "smb2.data_offset": "string",
    "smb2.domain": "string",
    "smb2.fid": "string",
    "smb2.filename": "string",
    "smb2.header_len": "string",
    "smb2.host": "string",
    "smb2.msg_id": "string",
    "smb2.pid": "string",
    "smb2.previous_sesid": "string",
    "smb2.protocol_id": "string",
    "smb2.sesid": "string",
    "smb2.session_flags": "string",
    "smb2.tid": "string",
    "smb2.write_length": "string",
    "dhcp": "string",
    "dhcp.client_id.duid_ll_hw_type": "string",
    "dhcp.cookie": "string",
    "dhcp.hw.addr_padding": "string",
    "dhcp.hw.mac_addr": "string",
    "dhcp.id": "string",
    "dhcp.ip.client": "string",
    "dhcp.ip.relay": "string",
    "dhcp.ip.server": "string",
    "dhcp.option.broadcast_address": "string",
    "dhcp.option.dhcp_server_id": "string",
    "dhcp.option.router": "string",
    "dhcp.option.vendor.bsdp.message_type": "string",
    "mdns": "string",
    "dns": "string",
    "dns.a": "string",
    "dns.count.add_rr": "string",
    "dns.count.answers": "string",
    "dns.count.auth_rr": "string",
    "dns.count.labels": "string",
    "dns.count.queries": "string",
    "dns.flags.authoritative": "string",
    "dns.flags.checkdisable": "string",
    "dns.flags.opcode": "string",
    "dns.flags.response": "string",
    "dns.id": "string",
    "dns.ptr.domain_name": "string",
    "dns.qry.name": "string",
    "dns.qry.name.len": "string",
    "dns.resp.len": "string",
    "dns.resp.name": "string",
    "dns.resp.ttl": "string",
    "dns.resp.len.1": "string",
    "dns.retransmit_request": "string",
    "dns.retransmit_response": "string",
    "dns.time": "category",
    "ssdp": "string",
    "http.connection": "string",
    "http.content_length": "string",
    "http.content_type": "string",
    "http.date": "string",
    "http.file_data": "string",
    "http.host": "string",
    "http.last_modified": "string",
    "http.location": "string",
    "http.next_request_in": "string",
    "http.next_response_in": "string",
    "http.request.full_uri": "string",
    "http.request.line": "string",
    "http.request.method": "string",
    "http.request.uri.path": "string",
    "http.request.uri.query": "string",
    "http.request.uri.query.parameter": "string",
    "http.request.version": "string",
    "http.request_in": "string",
    "http.response.code": "string",
    "http.response.code.desc": "string",
    "http.response.line": "string",
    "http.response.phrase": "string",
    "http.response.version": "string",
    "http.response_for.uri": "string",
    "http.response_in": "string",
    "http.referer": "string",
    "http.time": "string",
    "http.server": "string",
    "json.value.string": "string",
    "json.key": "string",
    "ssh.cookie": "string",
    "ssh.compression_algorithms_client_to_server_length": "string",
    "ssh.compression_algorithms_server_to_client_length": "string",
    "ssh.direction": "string",
    "ssh.dh_gex.max": "string",
    "ssh.dh_gex.min": "string",
    "ssh.dh_gex.nbits": "string",
    "ssh.encryption_algorithms_client_to_server_length": "string",
    "ssh.encryption_algorithms_server_to_client_length": "string",
    "ssh.host_key.length": "string",
    "ssh.host_key.type_length": "string",
    "ssh.kex_algorithms_length": "string",
    "ssh.mac_algorithms_client_to_server_length": "string",
    "ssh.mac_algorithms_server_to_client_length": "string",
    "ssh.message_code": "string",
    "ssh.mpint_length": "string",
    "ssh.packet_length": "string",
    "ssh.packet_length_encrypted": "string",
    "ssh.padding_length": "string",
    "ssh.padding_string": "string",
    "ssh.protocol": "string",
    "ssh.server_host_key_algorithms_length": "string",
    "tls.alert_message.desc": "string",
    "tls.alert_message.level": "string",
    "tls.app_data_proto": "string",
    "tls.compress_certificate.compressed_certificate_message.length": "string",
    "tls.connection_id": "string",
    "tls.handshake.extension.type": "string",
    "tls.handshake.extensions_key_share_group": "string",
    "tls.handshake.session_ticket_length": "string",
    "tls.handshake.version": "string",
    "tls.record.content_type": "string",
    "tls.record.version": "string",
    "Label": "category",
}



# from constants import dtypes_final, dtypes_categorical
# df = dd.read_csv("clean1.csv", dtype=dtypes_categorical)  # type: ignore
# df = df.drop(columns=["frame.number", "frame.time", "wlan.da", "wlan.ra", "wlan.sa", "wlan.ta", "wlan.fixed.reason_code", "wlan.seq", "wlan.bssid"])
# df = encode_binary(df)
# df = fill_missing(df)
# df.to_csv("clean4.csv", index=False, single_file=True)


clean5 = dd.read_csv("datasets/clean1.csv", dtype=dtypes_categorical)
clean5 = clean5.drop(columns=["frame.number", "frame.time", "wlan.da", "wlan.ra", "wlan.sa", "wlan.ta", "wlan.fixed.reason_code", "wlan.seq", "wlan.bssid"])

clean5.to_csv("clean5.csv", index=False, single_file=True)

