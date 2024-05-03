CREATE TABLE IF NOT EXISTS blocks (
    block_id serial PRIMARY KEY,
    block_hash VARCHAR(100) NOT NULL,
	chain_id VARCHAR(100) NOT NULL,
	height INTEGER NOT NULL,
	create_time TIMESTAMP NOT NULL
	CONSTRAINT blocks_pkey PRIMARY KEY (block_id)
	);
    

CREATE TABLE IF NOT EXISTS transactions (
    transac_id serial PRIMARY KEY,
    block_id INTEGER NOT NULL,
    memo VARCHAR(100) NOT NULL,
    fee_amount INTEGER NOT NULL,
    fee_denom VARCHAR(100) NOT NULL,
    gas_limit INTEGER NOT NULL,
    tx jsonb NOT NULL,
    CONSTRAINT transactions_pkey PRIMARY KEY (transac_id),
    CONSTRAINT transactions_block_id_fkey FOREIGN KEY (block_id)
        REFERENCES blocks (block_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
);


CREATE TABLE IF NOT EXISTS transc_types(
    type_id serial PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    type_message VARCHAR(100) NOT NULL,
    CONSTRAINT transc_types_pkey PRIMARY KEY (type_id)
);


INSERT INTO transc_types (type_message, type_name) VALUES
    ('/cosmos.authz.v1beta1.MsgExec', 'cosmos_exec_msg'),
    ('/ibc.core.client.v1.MsgUpdateClient', 'ibc_updateclient_msg'),
    ('/ibc.applications.transfer.v1.MsgTransfer', 'ibc_transfer_msg'),
    ('/cosmwasm.wasm.v1.MsgExecuteContract', 'cosmwasm_executecontract_msg'),
    ('/cosmos.staking.v1beta1.MsgDelegate', 'cosmos_delegate_msg'),
    ('/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward', 'cosmos_withdrawdelegatorreward_msg'),
    ('/cosmos.bank.v1beta1.MsgSend', 'cosmos_send_msg'),
    ('/alliance.alliance.MsgClaimDelegationRewards', 'alliance_claimdelegationrewards_msg'),
    ('/cosmos.authz.v1beta1.MsgGrant', 'cosmos_grant_msg'),
    ('/cosmos.staking.v1beta1.MsgUndelegate', 'cosmos_undelegate_msg'),
    ('/alliance.alliance.MsgDelegate', 'alliance_delegate_msg'),
    ('/cosmos.staking.v1beta1.MsgBeginRedelegate', 'cosmos_beginredelegate_msg'),
    ('/alliance.alliance.MsgUndelegate', 'alliance_undelegate_msg'),
    ('/cosmos.authz.v1beta1.MsgRevoke', 'cosmos_revoke_msg'),
    ('/cosmwasm.wasm.v1.MsgStoreCode', 'cosmwasm_storecode_msg'),
    ('/cosmwasm.wasm.v1.MsgInstantiateContract', 'cosmwasm_instantiatecontract_msg'),
    ('/alliance.alliance.MsgRedelegate', 'alliance_redelegate_msg'),
    ('/cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission', 'cosmos_withdrawvalidatorcommission_msg'),
    ('/ibc.core.channel.v1.MsgAcknowledgement', 'ibc_acknowledgement_msg'),
    ('/ibc.core.channel.v1.MsgRecvPacket', 'ibc_recvpacket_msg'),
    ('/ibc.core.channel.v1.MsgTimeout', 'ibc_timeout_msg'),
    ('/ibc.core.channel.v1.MsgChannelOpenConfirm', 'ibc_channelopenconfirm_msg'),
    ('/ibc.core.channel.v1.MsgChannelOpenTry', 'ibc_channelopentry_msg'),
    ('/cosmos.staking.v1beta1.MsgEditValidator', 'cosmos_editvalidator_msg');

CREATE TABLE IF NOT EXISTS transc_delegate_msg(
    msg_id serial PRIMARY KEY,
    transac_id INTEGER NOT NULL,
    delegator_address VARCHAR(100) NOT NULL,
    validator_address VARCHAR(100) NOT NULL,
    denom VARCHAR(100) NOT NULL,
    amount VARCHAR(100) NOT NULL,
    CONSTRAINT transc_delegate_msg_pkey PRIMARY KEY (msg_id),
    CONSTRAINT transc_delegate_msg_transac_id_fkey FOREIGN KEY (transac_id)
        REFERENCES transactions (transac_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS transc_grant_msg(
    msg_id serial PRIMARY KEY,
    transac_id INTEGER NOT NULL,
    granter VARCHAR(100) NOT NULL,
    grantee VARCHAR(100) NOT NULL,
    authorization_type VARCHAR(100) NOT NULL,
    allow_list jsonb,
    msg VARCHAR,
    expiration VARCHAR(100) NOT NULL,
    CONSTRAINT transc_grant_msg_pkey PRIMARY KEY (msg_id),
    CONSTRAINT transc_grant_msg_transac_id_fkey FOREIGN KEY (transac_id)
        REFERENCES transactions (transac_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS transc_transfer_msg(
    msg_id serial PRIMARY KEY,
    transac_id INTEGER NOT NULL,
    sender VARCHAR(100) NOT NULL,
    receiver VARCHAR(100) NOT NULL,
    source_channel VARCHAR(100) NOT NULL,
    denom VARCHAR(100) NOT NULL,
    amount VARCHAR(100) NOT NULL,
    CONSTRAINT transc_transfer_msg_pkey PRIMARY KEY (msg_id),
    CONSTRAINT transc_transfer_msg_transac_id_fkey FOREIGN KEY (transac_id)
        REFERENCES transactions (transac_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS transc_revoke_msg(
    msg_id serial PRIMARY KEY,
    transac_id INTEGER NOT NULL,
    granter VARCHAR(100) NOT NULL,
    grantee VARCHAR(100) NOT NULL,
    msg_type_url VARCHAR(100) NOT NULL,
    CONSTRAINT transc_revoke_msg_pkey PRIMARY KEY (msg_id),
    CONSTRAINT transc_revoke_msg_transac_id_fkey FOREIGN KEY (transac_id)
        REFERENCES transactions (transac_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS transc_beginredelegate_msg(
    msg_id serial PRIMARY KEY,
    transac_id INTEGER NOT NULL,
    delegator_address VARCHAR(100) NOT NULL,
    validator_src_address VARCHAR(100) NOT NULL,
    validator_dst_address VARCHAR(100) NOT NULL,
	denom VARCHAR(100) NOT NULL,
	amount VARCHAR(100) NOT NULL,
    CONSTRAINT transc_beginredelegate_msg_pkey PRIMARY KEY (msg_id),
    CONSTRAINT transc_beginredelegate_msg_transac_id_fkey FOREIGN KEY (transac_id)
        REFERENCES transactions (transac_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS transc_withdraovalidatorcommission_msg(
    msg_id serial PRIMARY KEY,
    transac_id INTEGER NOT NULL,
    validator_address VARCHAR(100) NOT NULL,
    CONSTRAINT transc_withdraovalidatorcommission_msg_pkey PRIMARY KEY (msg_id),
    CONSTRAINT transc_withdraovalidatorcommission_msg_transac_id_fkey FOREIGN KEY (transac_id)
        REFERENCES transactions (transac_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);